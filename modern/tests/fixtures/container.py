import tempfile

import pytest
from utils.docker_container import run_container


@pytest.fixture(scope="session")
def container(pytestconfig):
    image = pytestconfig.getoption("image")
    volumes_from = pytestconfig.getoption("volumes_from")
    user = pytestconfig.getoption("user")
    print(f">> Run image '{image}' using volumes-from '{volumes_from}' on user '{user}'")

    with run_container(image, volumes_from, user) as container:
        yield container
