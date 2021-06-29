import os.path
import re
from dataclasses import dataclass
from collections import defaultdict

import pytest
import yaml


@dataclass
class Version:
    full_version: str
    major: str
    minor: str = None
    patch: str = None

    def __init__(self, full_version=None):
        if not full_version:
            return

        self.full_version = full_version
        self.major, *rest = self.full_version.split('.', 1)
        if rest:
            self.minor, *rest = rest[0].split('.', 1)
            if rest:
                self.patch = rest[0]

    def __str__(self):
        ret = f"{self.major}"
        if self.minor is not None:
            ret += f".{self.minor}"
        if self.patch is not None:
            ret += f".{self.patch}"
        return ret

    def __lt__(self, other):
        return self.lazy_lt_semver(other)

    def lazy_lt_semver(self, other):
        lv1 = [int(v) for v in self.full_version.split(".")]
        lv2 = [int(v) for v in other.full_version.split(".")]
        min_length = min(len(lv1), len(lv2))
        return lv1[:min_length] < lv2[:min_length]


@dataclass
class Distro:
    name: str
    version: Version


@dataclass
class Compiler:
    name: str
    version: Version


@dataclass
class Expected:
    distro: Distro
    docker_username: str
    docker_tag: str
    python: Version
    cmake: Version
    conan: Version = None
    compiler: Compiler = None
    compiler_versions: defaultdict(list) = None

    def __str__(self):
        return f"""
        Expected:
            - distro: {self.distro}
            - docker_username: {self.docker_username}
            - docker_tag: {self.docker_tag}
            - python: {self.python}
            - cmake: {self.cmake}
            - conan: {self.conan}
            - compiler: {self.compiler}
            - compiler_versions: {self.compiler_versions}
        """

    def vanilla_image(self):
        """ Returns the vanilla docker container corresponding to the distribution """
        return f"{self.distro.name}:{self.distro.version}"

    def compatible_images(self, libstdcpp=False, libcpp=False):
        """ Returns a list with the images that are compatible with the binaries generated in the expected distro """
        # TODO: This function is first class citizen in this repository, move it closer to ROOT
        # TODO: Some Clang can use GCC images and viceversa
        compiler_versions = self.compiler_versions[self.compiler.name]
        if self.compiler.name == 'gcc':
            if libstdcpp:
                # For GCC images, due to `libstdc++` version, they are only backward compatible.
                compat_versions = [v for v in compiler_versions if self.compiler.version < v]
            else:
                compat_versions = compiler_versions
            return [f'{self.docker_username}/gcc{v.major}-{self.distro.name}{self.distro.version}:{self.docker_tag}' for v in compat_versions]
        elif self.compiler.name == 'clang':
            if libcpp:
                # For Clang images using libc++ we have the same issue, only backward compatible
                compat_versions = [v for v in compiler_versions if self.compiler.version < v]
            else:
                # ... if using libstdc++, all our images use the same version
                compat_versions = compiler_versions
            return [f'{self.docker_username}/clang{v.major}-{self.distro.name}{self.distro.version}:{self.docker_tag}' for v in compat_versions]
        else:
            raise NotImplemented


def get_compiler_versions(env_values):
    compiler_versions = defaultdict(list)
    for key, value in env_values.items():
        m_gcc = re.match(r'GCC\d+_VERSION', key)
        m_clang = re.match('CLANG\d+_VERSION', key)
        if m_gcc:
            compiler_versions['gcc'].append(Version(value))
        elif m_clang:
            compiler_versions['clang'].append(Version(value))
        else:
            pass
    return compiler_versions


@pytest.fixture(scope="session")
def expected(request) -> Expected:
    # Parse the image filename
    image = request.config.option.image
    m = re.match(r'((?P<domain>[\w\-.]+)\/)?'
                 r'(?P<username>[\w\-.]+)\/'
                 r'((?P<compiler>gcc|clang)(?P<version>\d+)-)?'
                 r'((?P<service>base|builder|deploy|conan)-)?'
                 r'(?P<distro>[a-z]+)(?P<distro_version>[\d.]+)'
                 r'(-(?P<jenkins>jenkins))?'
                 r'(:(?P<tag>[\w\-.]+))?', image)

    # Parse the envfile used to generate the docker images
    envfile = request.config.option.env_file
    env_values = {}
    with open(envfile, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                print(line)
                key, value = line.split('=')
                env_values[key] = value

    distro = Distro(m.group('distro'), Version(m.group('distro_version')))
    python = Version(env_values.get('PYTHON_VERSION'))
    cmake = Version(env_values.get('CMAKE_VERSION_FULL'))
    expected = Expected(distro, m.group('username'), m.group('tag'), python, cmake)
    expected.conan = Version(env_values.get('CONAN_VERSION'))
    expected.compiler_versions = get_compiler_versions(env_values)

    if m.group('compiler'):
        compiler = m.group('compiler')
        major = m.group('version')
        full_version = env_values.get(f"{compiler.upper()}{major}_VERSION")
        expected.compiler = Compiler(compiler, Version(full_version))

    print(expected)
    return expected


@pytest.fixture(autouse=True)
def skip_by_compiler(request, expected):
    if request.node.get_closest_marker('compiler'):
        if request.node.get_closest_marker('compiler').args[0] != expected.compiler.name:
            pytest.skip('skipped for this compiler: {}'.format(expected.compiler.name))
