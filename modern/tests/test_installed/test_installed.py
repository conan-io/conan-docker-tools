def test_cmake_version(container, expected):
    output, _ = container.exec(['cmake', '--version'])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f'cmake version {expected.cmake}'


def test_python_version(container, expected):
    output, _ = container.exec(['python', '--version'])
    assert output.strip() == f'Python {expected.python}'
