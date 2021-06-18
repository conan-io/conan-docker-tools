import pytest


@pytest.mark.compiler('clang')
@pytest.mark.service('builder', 'deploy', 'jenkins')
class TestClangCompiler:

    def test_version(self, container, expected):
        out, err = container.exec(['clang', '--version'])
        first_line = out.splitlines()[0]
        assert first_line == f"clang version {expected.compiler.version}", f"out: '{out}' err: '{err}'"
