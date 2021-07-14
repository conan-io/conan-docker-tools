import pytest


@pytest.mark.parametrize(
    "tool",
    [
        "vim",
        "vi",
        "nano",
        "meson",
        "ninja",
        "bazel",
        "scons",
        "qmake",
        "xmake",
        "premake5",
        "b2",
        "java",
        "lua",
    ],
)
def test_not_installed(container, tool):
    output, _ = container.exec([tool, "--version"])
    first_line = output.splitlines()[0]
    assert f'exec: \\"{tool}\\": executable file not found in $PATH' in first_line.strip()
