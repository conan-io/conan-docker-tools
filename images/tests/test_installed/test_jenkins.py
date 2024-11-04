import pytest


@pytest.mark.service('jenkins')
class TestJenkinsAgent:

    def test_java(self, container):
        out, err = container.exec(['java', '-version'])
        # TODO: Pass expected JDK version as parameter. For now, we know it's 11 and we don't need to update it.
        assert 'openjdk version "11.' in err, f"out: '{out}' err: '{err}'"

    def test_agent(self, container):
        """The Jenkins agent version should match the image tag version
        """
        out, err = container.exec(['java', '-jar', '/usr/share/jenkins/agent.jar', '-version'])
        image = container.image
        assert out.strip() in image, f"out: '{out}' err: '{err}'"

    def test_entrypoint(self, container):
        out, err = container.exec(['/opt/entrypoint.sh', '-help'])
        # It shows help (missing arguments), but we know it works
        assert 'Show this help message' in out, f"out: '{out}' err: '{err}'"

    def test_cacert(self, container):
        out, err = container.exec(['keytool', '-list', '-keystore', '/etc/ssl/certs/java/cacerts', '-storepass', 'changeit', '-storetype', 'JKS'])
        assert 'Keystore type: JKS' in out, f"out: '{out}' err: '{err}'"
