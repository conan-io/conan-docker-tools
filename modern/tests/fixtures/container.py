import tempfile

import pytest
from utils.docker_container import run_container


@pytest.fixture(scope="session")
def container(pytestconfig):
    image = pytestconfig.getoption("image")
    volumes_from = pytestconfig.getoption("volumes_from")
    working_dir = pytestconfig.getoption("working_dir")
    print(f">> Run image '{image}' using volumes-from '{volumes_from}' on wdir '{working_dir}'")

    with run_container(image, volumes_from, working_dir) as container:
        yield container
