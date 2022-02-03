import os.path
import re
import pytest
from collections import defaultdict
from dataclasses import dataclass

from utils.version import Version


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
    suffix: str = None

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
            - suffix: {self.suffix}
        """

    def vanilla_image(self):
        """ Returns the vanilla docker container corresponding to the distribution """
        return f"{self.distro.name}:{self.distro.version}"

    def image_name(self, compiler, version):
        suffix = f'-{self.suffix}' if self.suffix else ''
        return f'{self.docker_username}/{compiler}{version.major}-{self.distro.name}{self.distro.version}{suffix}:{self.docker_tag}'


def get_compiler_versions():
    env_values = get_envfile_values()
    compiler_versions = defaultdict(list)
    for key, value in env_values.items():
        m_gcc = re.match(r'GCC\d+_VERSION', key)
        m_clang = re.match(r'CLANG\d+_VERSION', key)
        if m_gcc:
            compiler_versions['gcc'].append(Version(value))
        elif m_clang:
            compiler_versions['clang'].append(Version(value))
        else:
            pass
    return compiler_versions


def get_envfile_values():
    envfile = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
    env_values = {}
    with open(envfile, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                print(line)
                key, value = line.split('=')
                env_values[key] = value
    return env_values


@pytest.fixture(scope="session")
def expected(request) -> Expected:
    # Parse the image filename
    image = request.config.option.image
    m = re.match(r'((?P<domain>[\w\-.]+)\/)?'
                 r'(?P<username>[\w\-.]+)\/'
                 r'((?P<compiler>gcc|clang)(?P<version>\d+))?'
                 r'(?P<service_base>base)?'
                 r'-(?P<distro>[a-z]+)(?P<distro_version>[\d.]+)'
                 r'(-(?P<suffix>cci))?'
                 r'(-(?P<service>builder|jenkins))?'
                 r'(:(?P<tag>[\w\-.]+))?', image)

    # Parse the envfile used to generate the docker images
    env_values = get_envfile_values()

    distro = Distro(m.group('distro'), Version(m.group('distro_version')))
    python = Version(env_values.get('PYTHON_VERSION'))
    cmake = Version(env_values.get('CMAKE_VERSION_FULL'))
    expected = Expected(distro, m.group('username'), m.group('tag'), python, cmake)
    expected.conan = Version(env_values.get('CONAN_VERSION'))
    expected.compiler_versions = get_compiler_versions()
    expected.suffix = m.group('suffix')

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
