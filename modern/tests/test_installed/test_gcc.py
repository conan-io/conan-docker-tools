import pytest


@pytest.mark.compiler('gcc')
@pytest.mark.service('builder', 'deploy', 'jenkins')
class TestGccCompiler:

    def test_version(self, container, expected):
        out, _ = container.exec(['gcc', '--version'])
        assert expected.compiler.name == 'gcc'
        first_line = out.splitlines()[0]
        assert first_line == f'gcc (GCC) {expected.compiler.version}'

    def test_gfortran_version(self, container, expected):
        out, _ = container.exec(['gfortran', '--version'])
        assert expected.compiler.name == 'gcc'
        first_line = out.splitlines()[0]
        assert first_line == f'GNU Fortran (GCC) {expected.compiler.version}'
