def test_conan_version(container, expected):
    out, err = container.exec(['conan', '--version'])
    assert out.strip() == f'Conan version {expected.conan}', f"out: '{out}' err: '{err}'"

def test_revisions_enabled(container):
    out, _ = container.exec(['conan', '--version'])
    if "Conan version 1." in out.strip():
        out, err = container.exec(['conan', 'config', 'get', 'general.revisions_enabled'])
        assert out.strip() == '1', f"out: '{out}' err: '{err}'"

def test_default_libcxx(container):
    out, err = container.exec(['conan', 'profile', 'show', 'default'])
    if 'compiler=gcc' in out:
        assert 'compiler.libcxx=libstdc++' in out, f"out: '{out}' err: '{err}'"

# TODO: Add more tests here:
#   * default profiles exists, and it has proper libcxx value
#   * python version used by Conan
