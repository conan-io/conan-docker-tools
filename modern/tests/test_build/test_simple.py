import pytest
from fixtures.container import run_container
from fixtures.expected import get_compiler_versions, Version


# Checks that a very simple C and C++ project can be built using these images
# It also checks the libraries the project was linked with and that
# the binary generated can run in a vanilla image


@pytest.fixture(autouse=True, scope='class')
def _build_simple(request, container, expected):
    build_directory = 'modern/tests/tmp/simple'
    request.cls._build_directory = build_directory

    with container.working_dir(build_directory):
        container.exec(['cmake', '../../workingdir/simple', '-DCMAKE_BUILD_TYPE=Release'])
        container.exec(['cmake', '--build', '.'])


class TestBuildSimple:

    @pytest.mark.service('deploy', 'jenkins')
    def test_running_container(self, container, expected):
        # Compile the project
        with container.working_dir(self._build_directory):
            # Check it runs
            out, err = container.exec(['./example-c'])
            assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"
            out, err = container.exec(['./example-cpp'])
            assert 'Current date' in out, f"out: '{out}' err: '{err}'"

            # Check linked libs
            out, err = container.exec(['ldd', 'example-c'])
            # TODO: Test linked libraries here (gcc)
            print(out)
            print(err)

            out, err = container.exec(['ldd', 'example-cpp'])
            # TODO: Test linked libraries here (gcc)
            print(out)
            print(err)

    @pytest.mark.service('deploy', 'jenkins')
    def test_vanilla_image(self, container, expected):
        # C executable should run in vanilla image
        with container.run_container(expected.vanilla_image()) as vanilla:
            with vanilla.working_dir(self._build_directory):
                out, err = vanilla.exec(['./example-c'])
                assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"

    @pytest.mark.service('xtest')
    @pytest.mark.parametrize("compiler, compiler_version", [(key, str(v)) for key, value in get_compiler_versions().items() for v in value])
    def test_c_compatible(self, container, expected, compiler, compiler_version):
        # C executable should run in all the containers
        image_name = expected.image_name(compiler, Version(compiler_version))
        with container.run_container(image_name) as image:
            with image.working_dir(self._build_directory):
                out, err = image.exec(['./example-c'])
                assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"

    @pytest.mark.service('xtest')
    @pytest.mark.parametrize("compiler, compiler_version", [(key, str(v)) for key, value in get_compiler_versions().items() for v in value])
    def test_cpp_compatible(self, container, expected, compiler, compiler_version):
        # CXX executable requires C++ standard lib installed. There are some rules
        version = Version(compiler_version)
        if compiler == expected.compiler.name and version < expected.compiler.version:
            pytest.skip(f'Cannot run if same compiler and lower version')

        # TODO: We need to bypass some GCC/Clang versions (failure expected)

        image_name = expected.image_name(compiler, version)
        with container.run_container(image_name) as image:
            with image.working_dir(self._build_directory):
                out, err = image.exec(['./example-cpp'])
                assert 'Current date' in out, f"out: '{out}' err: '{err}'"


"""
@pytest.mark.compiler('gcc')
@pytest.mark.service('deploy', 'jenkins')
def test_gcc_simple(container, expected):
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
        out, err = container.exec(['ldd', 'example-c'])
        # TODO: Test linked libraries here (gcc)
        print(out)
        print(err)

        out, err = container.exec(['ldd', 'example-cpp'])
        # TODO: Test linked libraries here (gcc)
        print(out)
        print(err)

    # C executable should run in vanilla image
    with run_container(expected.vanilla_image(), tmpdirname=container._tmpfolder) as vanilla:
        with vanilla.working_dir(build_directory):
            out, err = vanilla.exec(['./example-c'])
            assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"

    # CPP can only run in newer images with GCC installed
    compat_images = expected.compatible_images(libstdcpp=True)
    print(f"Run executable in compatible images {', '.join(compat_images)}")
    for it in compat_images:
        with run_container(it, tmpdirname=container._tmpfolder) as image:
            with image.working_dir(build_directory):
                out, err = image.exec(['./example-c'])
                assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"

                out, err = image.exec(['./example-cpp'])
                assert 'Current date' in out, f"out: '{out}' err: '{err}'"


@pytest.mark.compiler('clang')
@pytest.mark.service('deploy', 'jenkins')
def test_clang_simple(container, expected):
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
        out, err = container.exec(['ldd', 'example-c'])
        # TODO: Test linked libraries here (clang)
        print(out)
        print(err)

        out, err = container.exec(['ldd', 'example-cpp'])
        # TODO: Test linked libraries here (clang)
        print(out)
        print(err)

    # C executable should run in vanilla image
    with run_container(expected.vanilla_image(), tmpdirname=container._tmpfolder) as vanilla:
        with vanilla.working_dir(build_directory):
            out, err = vanilla.exec(['./example-c'])
            assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"

    # Clang uses libstdc++ by default, so it runs in all images
    compat_images = expected.compatible_images(libstdcpp=False, libcpp=False)
    print(f"Run executable in compatible images {', '.join(compat_images)}")
    for it in compat_images:
        with run_container(it, tmpdirname=container._tmpfolder) as image:
            with image.working_dir(build_directory):
                out, err = image.exec(['./example-c'])
                assert 'Current local time and date' in out, f"out: '{out}' err: '{err}'"

                out, err = image.exec(['./example-cpp'])
                assert 'Current date' in out, f"out: '{out}' err: '{err}'"
"""
