def test_conan_version(container, expected):
    out, err = container.exec(['conan', '--version'])
    assert out.rstrip() == f'Conan version {expected.conan}', f"out: '{out}' err: '{err}'"

# TODO: Add more tests here:
#   * default profiles exists, and it has proper libcxx value
#   * python version used by Conan
