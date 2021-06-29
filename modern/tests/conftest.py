import os

import pytest

docker_compose_services = ['base',
                           # 'builder',  This is just a helper image, do we need to test it?
                           'deploy',
                           'jenkins']

pytest_plugins = [
    "fixtures.container",
    "fixtures.expected",
]


def pytest_addoption(parser):
    parser.addoption("--image", action="store", required=True)
    parser.addoption("--service", action="store", choices=docker_compose_services)
    parser.addoption("--env-file", action="store", default=os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '.env')),
                     help="Path to the envfile used to generate the docker images")


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", f"service(name): executes tests only for the given service: {', '.join(docker_compose_services)}")
    config.addinivalue_line("markers", f"compiler(name): either gcc or clang")


def pytest_runtest_setup(item):
    envnames = [mark.args[0] for mark in item.iter_markers(name="service")]
    if envnames:
        opt = item.config.getoption("--service")
        if opt and opt not in envnames:
            pytest.skip("test requires service in {!r}".format(envnames))
