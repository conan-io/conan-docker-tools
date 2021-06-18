import pytest
from utils.docker_container import run_container


@pytest.mark.compiler('gcc')
@pytest.mark.service('builder', 'deploy', 'jenkins')
def test_gfortran(container, expected):
    build_directory = '/tmp/build/gfortran'
    # Compile the project
    with container.working_dir(build_directory):
        container.exec(['cmake', '/tmp/workingdir/gfortran', '-DCMAKE_BUILD_TYPE=Release'])
        container.exec(['cmake', '--build', '.'])

        out, err = container.exec(['./hello'])
        assert 'Hello world!' in out, f"out: '{out}' err: '{err}'"

    # Check we can run these executables in vanilla image
    vanilla_img = f"{expected.distro.name}:{expected.distro.version}"
    with run_container(vanilla_img, tmpdirname=container._tmpfolder) as vanilla:
        with vanilla.working_dir(build_directory):
            out, err = vanilla.exec(['./hello'])
            assert 'Hello world!' in out, f"out: '{out}' err: '{err}'"
