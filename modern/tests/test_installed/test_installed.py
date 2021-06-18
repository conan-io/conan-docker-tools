import pytest


def test_cmake_version(container, expected):
    output, _ = container.exec(['cmake', '--version'])
    first_line = output.splitlines()[0]
    assert first_line == f'cmake version {expected.cmake}'


def test_python_version(container, expected):
    output, _ = container.exec(['python', '--version'])
    assert output.rstrip() == f'Python {expected.python}'


@pytest.mark.service('jenkins')
def test_jenkins_agent_version(container, expected):
    # FIXME: I need to install unzip to unpack the slave.jar file, but I don't want to modify the image!
    container.exec(['sudo', 'apt-get', 'update'])
    container.exec(['sudo', 'apt-get', 'install', 'unzip'])

    output, err = container.raw_exec("/bin/bash -c 'unzip -p /usr/share/jenkins/slave.jar | head'")
    assert any([line == f'Version: {expected.jenkins_agent}' for line in output.splitlines()]), f"Not found in {output}"


@pytest.mark.service('jenkins')
def test_java_version(container, expected):
    output, _ = container.exec(['java', '-version'])
    first_line = output.splitlines()[0]
    assert first_line == 'openjdk version "1.8.0_292"'
