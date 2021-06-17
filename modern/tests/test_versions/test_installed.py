def test_cmake_version(container, expected):
    output, _ = container.exec(['cmake', '--version'])
    first_line = output.splitlines()[0]
    assert first_line == f'cmake version {expected.cmake}'
