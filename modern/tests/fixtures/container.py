import tempfile

import pytest
from utils.docker_container import run_container


@pytest.fixture(scope="session")
def container(pytestconfig):
    image = pytestconfig.getoption("image")
    with tempfile.TemporaryDirectory() as tmpdirname:
        with run_container(image, tmpdirname) as container:
            yield container
