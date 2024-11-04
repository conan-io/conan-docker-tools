import pytest

docker_compose_services = ['base',
                           # 'builder',  This is just a helper image, do we need to test it?
                           'deploy',
                           'jenkins',
                           'xtest']

pytest_plugins = [
    "fixtures.container",
    "fixtures.expected",
]


def pytest_addoption(parser):
    parser.addoption("--image", action="store", required=True)
    parser.addoption("--service", action="store", choices=docker_compose_services)
    parser.addoption("--volumes-from", action="store", help="ID of the docker container to mount volumes from. Used"
                                                            " in Jenkins.")
    parser.addoption("--user", action="store", help="user:group to run container. Used in Jenkins.")


def pytest_configure(config):
    # register an additional marker
    config.addinivalue_line("markers", f"service(name): executes tests only for the given service: {', '.join(docker_compose_services)}")
    config.addinivalue_line("markers", f"compiler(name): either gcc or clang")


def pytest_runtest_setup(item):
    envnames = []
    for mark in item.iter_markers(name="service"):
        envnames += mark.args

    if envnames:
        opt = item.config.getoption("--service")
        if opt and opt not in envnames:
            pytest.skip("test requires service in {!r}".format(envnames))
