import pytest


@pytest.mark.service('jenkins')
class TestJenkinsAgent:

    def test_java(self, container):
        # TODO: Pass expected JDK version as parameter
        out, err = container.exec(['java', '-version'])
        # Check Java, up to minor version
        assert 'openjdk version' in err, f"out: '{out}' err: '{err}'"

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
