import pytest
from fixtures.container import run_container


# Checks that a very simple C and C++ project can be built using these images
# It also checks the libraries the project was linked with and that
# the binary generated can run in a vanilla image


@pytest.mark.service('deploy', 'jenkins')
def test_simple(container, expected):
    build_directory = '/tmp/build/simple'
    # Compile the project
    with container.working_dir(build_directory):
        container.exec(['cmake', '/tmp/workingdir/simple', '-DCMAKE_BUILD_TYPE=Release'])
        container.exec(['cmake', '--build', '.'])

        # Check it runs
        out, err = container.exec(['./example-c'])
        assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"
        out, err = container.exec(['./example-cpp'])
        assert 'Current date' in out, f"out: '{out}' err: '{err}'"

        # Check linked libs

    # Check we can run these executables in vanilla image
    vanilla_img = f"{expected.distro.name}:{expected.distro.version}"
    with run_container(vanilla_img, tmpdirname=container._tmpfolder) as vanilla:
        with vanilla.working_dir(build_directory):
            out, err = vanilla.exec(['./example-c'])
            assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"

            out, err = vanilla.exec(['./example-cpp'])
            assert 'Current date' in out, f"out: '{out}' err: '{err}'"
