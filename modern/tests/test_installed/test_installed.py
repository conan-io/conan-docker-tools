def test_cmake_version(container, expected):
    output, _ = container.exec(['cmake', '--version'])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f'cmake version {expected.cmake}'


def test_python_version(container, expected):
    output, _ = container.exec(['python', '--version'])
    assert output.strip() == f'Python {expected.python}'


def test_pkg_config(container, expected):
    output, _ = container.exec(["pkg-config", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"{expected.pkg_config}"


def test_make(container, expected):
    output, _ = container.exec(["make", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"GNU Make {expected.make}"


def test_autoconf(container, expected):
    output, _ = container.exec(["autoconf", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"autoconf (GNU Autoconf) {expected.autoconf}"


def test_autoreconf(container, expected):
    output, _ = container.exec(["autoreconf", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"autoreconf (GNU Autoconf) {expected.autoconf}"


def test_perl(container, expected):
    output, _ = container.exec(["perl", "--version"])
    first_line = output.splitlines()[1]
    assert f"v{expected.perl}" in first_line.strip()


def test_wget(container, expected):
    output, _ = container.exec(["wget", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"GNU Wget {expected.wget} built on linux-gnu."


def test_curl(container, expected):
    output, _ = container.exec(["curl", "--version"])
    first_line = output.splitlines()[0]
    assert f"curl {expected.curl}" in first_line.strip()


def test_git(container, expected):
    output, _ = container.exec(["git", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"git version {expected.git}"


def test_subversion(container, expected):
    output, _ = container.exec(["svn", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"svn, version {expected.subversion} (r1718519)"


def test_xz_utils(container, expected):
    output, _ = container.exec(["xz", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"xz (XZ Utils) {expected.xzutils}"


def test_nasm(container, expected):
    output, _ = container.exec(["nasm", "-v"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"NASM version {expected.nasm}"
