import pytest


@pytest.mark.compiler('gcc')
@pytest.mark.service('deploy', 'jenkins')
class TestGccCompiler:

    @pytest.mark.parametrize('app', ['gcc', 'cc', 'cpp', 'c++', 'g++'])
    def test_version(self, container, expected, app):
        out, _ = container.exec([app, '--version'])
        first_line = out.splitlines()[0]
        assert first_line.strip() == f'{app} (GCC) {expected.compiler.version}'

    def test_gfortran_version(self, container, expected):
        out, _ = container.exec(['gfortran', '--version'])
        assert expected.compiler.name == 'gcc'
        first_line = out.splitlines()[0]
        assert first_line.strip() == f'GNU Fortran (GCC) {expected.compiler.version}'
