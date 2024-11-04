import pytest


@pytest.mark.compiler('clang')
@pytest.mark.service('deploy', 'jenkins')
class TestClangCompiler:

    def test_version(self, container, expected):
        out, err = container.exec(['clang', '--version'])
        first_line = out.splitlines()[0]
        assert first_line.strip() == f"clang version {expected.compiler.version}", f"out: '{out}' err: '{err}'"

    def test_libunwind_installed(self, container, expected):
        out, err = container.exec(['ldd', '/usr/local/lib/libllvm-unwind.so.1'])
        assert "libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1" in out, f"out: '{out}' err: '{err}'"

    def test_no_unwind_linked_on_libcpp(self, container, expected):
        out, err = container.exec(['ldd', '/usr/local/lib/libc++.so'])
        assert "libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1" in out, f"out: '{out}' err: '{err}'"
        assert "llvm-unwind" not in out, f"out: '{out}' err: '{err}'"

    def test_no_unwind_linked_on_libcppabi(self, container, expected):
        out, err = container.exec(['ldd', '/usr/local/lib/libc++abi.so'])
        assert "libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1" in out, f"out: '{out}' err: '{err}'"
        assert "llvm-unwind" not in out, f"out: '{out}' err: '{err}'"

    def test_no_unwind_linked_on_clang(self, container, expected):
        out, err = container.exec(['ldd', '/usr/local/bin/clang'])
        assert "libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1" in out, f"out: '{out}' err: '{err}'"
        assert "llvm-unwind" not in out, f"out: '{out}' err: '{err}'"

    def test_no_unwind_linked_on_clangpp(self, container, expected):
        out, err = container.exec(['ldd', '/usr/local/bin/clang++'])
        assert "libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1" in out, f"out: '{out}' err: '{err}'"
        assert "llvm-unwind" not in out, f"out: '{out}' err: '{err}'"
