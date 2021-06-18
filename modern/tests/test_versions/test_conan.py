def test_conan_version(container, expected):
    output, _ = container.exec(['conan', '--version'])
    assert output.rstrip() == f'Conan version {expected.conan}'

# TODO: Add more tests here:
#   * default profiles exists, and it has proper libcxx value
#   * python version used by Conan
