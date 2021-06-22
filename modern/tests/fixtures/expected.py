import os.path
import re
from dataclasses import dataclass

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
    python: Version
    cmake: Version
    conan: Version = None
    compiler: Compiler = None

    def vanilla_image(self):
        """ Returns the vanilla docker container corresponding to the distribution """
        return f"{self.distro.name}:{self.distro.version}"

    def compatible_images(self, libstdcpp=False, libcpp=False):
        """ Returns a list with the images that are compatible with the binaries generated in the expected distro """
        # TODO: This function is first class citizen in this repository, move it closer to ROOT
        compiler_versions = get_compiler_versions(self.compiler.name)
        if self.compiler.name == 'gcc':
            if libstdcpp:
                # For GCC images, due to `libstdc++` version, they are only backward compatible.
                compat_versions = [v for v in compiler_versions if self.compiler.version < v]
            else:
                compat_versions = compiler_versions
            return [f'gcc{v.major}-{self.distro.name}{self.distro.version}:{self.conan.full_version}' for v in compat_versions]
        elif self.compiler.name == 'clang':
            if libcpp:
                # For Clang images using libc++ we have the same issue, only backward compatible
                compat_versions = [v for v in compiler_versions if self.compiler.version < v]
            else:
                # ... if using libstdc++, all our images use the same version
                compat_versions = compiler_versions
            return [f'clang{v.major}-{self.distro.name}{self.distro.version}:{self.conan.full_version}' for v in compat_versions]
        else:
            raise NotImplemented


def get_compiler_versions(compiler_name):
    docker_file = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'docker-compose.yml'))
    with open(docker_file, 'r') as f:
        data = yaml.safe_load(f)

    if compiler_name == 'gcc':
        keys = [k for k in data.keys() if 'x-gcc' in k]
        return [Version(data.get(k).get('GCC_VERSION')) for k in keys]
    elif compiler_name == 'clang':
        keys = [k for k in data.keys() if 'x-llvm' in k]
        return [Version(data.get(k).get('LLVM_VERSION')) for k in keys]
    else:
        raise NotImplemented


def get_compiler_version(compiler_name, compiler_major):
    docker_file = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', 'docker-compose.yml'))
    with open(docker_file, 'r') as f:
        data = yaml.safe_load(f)

    if compiler_name == 'gcc':
        return data.get(f'x-gcc{compiler_major}').get('GCC_VERSION')
    elif compiler_name == 'clang':
        return data.get(f'x-llvm{compiler_major}').get('LLVM_VERSION')
    else:
        raise NotImplemented


@pytest.fixture(scope="session")
def expected(request) -> Expected:
    # Parse the image filename
    image = request.config.option.image
    m = re.match(r'((?P<domain>[\w.]+)\/)?'
                 r'(?P<username>[\w.]+)\/'
                 r'((?P<compiler>gcc|clang)(?P<version>\d+)-)?'
                 r'((?P<service>base|builder|deploy|conan)-)?'
                 r'(?P<distro>[a-z]+)(?P<distro_version>[\d.]+)'
                 r'(-(?P<jenkins>jenkins))?'
                 r'(:(?P<conan>[\d.]+))?', image)

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
    expected = Expected(distro, python, cmake)

    if m.group('conan'):
        expected.conan = Version(m.group('conan'))
        assert str(expected.conan) == env_values.get('CONAN_VERSION')

    if m.group('compiler'):
        compiler = m.group('compiler')
        major = m.group('version')
        full_version = get_compiler_version(compiler, major)
        expected.compiler = Compiler(compiler, Version(full_version))

    return expected


@pytest.fixture(autouse=True)
def skip_by_compiler(request, expected):
    if request.node.get_closest_marker('compiler'):
        if request.node.get_closest_marker('compiler').args[0] != expected.compiler.name:
            pytest.skip('skipped for this compiler: {}'.format(expected.compiler.name))
