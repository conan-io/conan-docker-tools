import pytest
from fixtures.expected import get_compiler_versions, Version


# Checks that a very simple Fortran project can be built using these images
# It also checks the libraries the project was linked with and that
# the binary generated can run in a vanilla image and _newer_ images


@pytest.fixture(autouse=True, scope='class')
def _build_simple(request, container, expected):
    build_directory = 'modern/tests/tmp/gfortran'
    request.cls._build_directory = build_directory

    with container.working_dir(build_directory):
        container.exec(['cmake', '../../workingdir/gfortran', '-DCMAKE_BUILD_TYPE=Release'])
        container.exec(['cmake', '--build', '.'])


@pytest.mark.compiler('gcc')
class TestBuildGFortran:

    @pytest.mark.service('deploy', 'jenkins')
    def test_running_container(self, container, expected):
        # Compile the project
        with container.working_dir(self._build_directory):
            # Check it runs
            out, err = container.exec(['./hello'])
            assert 'Hello world!' in out, f"out: '{out}' err: '{err}'"

            # Check linked libs
            out, err = container.exec(['ldd', 'hello'])
            # TODO: Test linked libraries here (gcc)
            print(out)
            print(err)

    @pytest.mark.xfail(reason="Runtime is not available in vanilla images, neither easily installable using apt")
    @pytest.mark.service('deploy', 'jenkins')
    def test_vanilla_image(self, container, expected):
        # C executable should run in vanilla image
        with container.run_container(expected.vanilla_image()) as vanilla:
            with vanilla.working_dir(self._build_directory):
                out, err = vanilla.exec(['./hello'])
                assert 'Hello world!' in out, f"out: '{out}' err: '{err}'"

    @pytest.mark.xfail(reason="Each binary requires each own version of 'libgfortran.so.<v>' and it isn't backward compatible")
    @pytest.mark.service('xtest')
    @pytest.mark.parametrize("compiler, compiler_version", [(key, str(v)) for key, value in get_compiler_versions().items() for v in value])
    def test_compatible(self, container, expected, compiler, compiler_version):
        # Fortran executable requires GCC (gfortran) installed
        if compiler != "gcc":
            pytest.skip('Requires GCC installed')

        image_name = expected.image_name(compiler, Version(compiler_version))
        with container.run_container(image_name) as image:
            with image.working_dir(self._build_directory):
                out, err = image.exec(['./hello'])
                assert 'Hello world!' in out, f"out: '{out}' err: '{err}'"
