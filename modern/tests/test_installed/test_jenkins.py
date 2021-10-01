import pytest


@pytest.mark.service('jenkins')
class TestJenkinsAgent:

    def test_java(self, container):
        out, _ = container.exec(['java', '-version'])
        first_line = out.splitlines()[0]
        # Check Java, up to minor version
        assert 'openjdk version "1.8' in first_line.strip()

    def test_entrypoint(self):
        out, _ = container.exec(['/opt/entrypoint.sh'])
        # It shows help (missing arguments), but we know it works
        assert 'java -jar agent.jar [options...] <secret key> <agent name>' in out
