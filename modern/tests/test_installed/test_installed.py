import pytest


expected_versions = {
    "pkg-config": {"16.04": "0.29.1"},
    "make": {"16.04": "4.1"},
    "autoconf": {"16.04": "2.69"},
    "autoreconf": {"16.04": "2.69"},
    "perl": {"16.04": "5.22.1"},
    "wget": {"16.04": "1.17.1"},
    "curl": {"16.04": "7.47.0"},
    "git": {"16.04": "2.34.1"},
    "svn": {"16.04": "1.9.3"},
    "xz": {"16.04": "5.1.0"},
    "nasm": {"16.04": "2.11.08"},
    "ar": {"16.04": "2.37"},
    "objdump": {"16.04": "2.37"},
    "readelf": {"16.04": "2.37"},
}


def test_cmake_version(container, expected):
    output, _ = container.exec(["cmake", "--version"])
    first_line = output.splitlines()[0]
    assert first_line.strip() == f"cmake version {expected.cmake}"


def test_python_version(container, expected):
    output, _ = container.exec(["python", "--version"])
    assert output.strip() == f"Python {expected.python}"


@pytest.mark.parametrize("tool", expected_versions.keys())
def test_installed_system_package_version(container, expected, tool):
    output, _ = container.exec([tool, "--version"])
    if output == "":
        output, _ = container.exec([tool, "-v"])
    assert expected_versions[tool][expected.distro.version.full_version] in output
