#!/bin/bash

set -ex

python --version
pip --version
cmake --version
conan --version
cpp --version
cc --version

export CONAN_USER_HOME=/tmp/conan
export CONAN_PRINT_RUN_COMMANDS=1

mkdir -p /tmp/build
rm -rf /tmp/build/*

conan config init --force

pushd /tmp/build

conan create /tmp/project/test/clang/conan foo/0.1@user/testing --build -s compiler.libcxx=libc++ -s build_type=Debug
conan install foo/0.1@user/testing -g deploy -s compiler.libcxx=libc++ -s build_type=Debug

bin/foobar_c
bin/foobar

ldd bin/foobar | grep 'libc++.so.1 => /usr/local/lib/libc++.so.1'
ldd bin/foobar | grep 'libllvm-unwind.so.1 => /usr/local/lib/libllvm-unwind.so.1'
ldd bin/foobar | grep -v 'libgcc'

mv bin/foobar bin/foobar_cpp_libcpp
mv bin/foobar_c bin/foobar_c_libcpp

cp /usr/local/lib64/libstdc++.so.6.0.28 bin/libstdc++.so.6.0.28
cp /usr/local/lib64/libatomic.so.1.2.0 bin/libatomic.so.1.2.0
cp /usr/local/lib/libllvm-unwind.so.1.0 bin/libllvm-unwind.so.1.0

cp /usr/local/lib/libllvm-unwind.so.1.0 bin/libunwind.so.1.0
cp /usr/local/lib/libc++.so.1.0 bin/libc++.so.1.0
cp /usr/local/lib/libc++abi.so.1.0 bin/libc++abi.so.1.0

conan create /tmp/project/test/clang/conan foo/0.1@user/testing --build -s compiler.libcxx=libstdc++ -s build_type=Debug
conan install foo/0.1@user/testing -g deploy -s compiler.libcxx=libstdc++ -s build_type=Debug

bin/foobar_c
bin/foobar

ldd bin/foobar | grep -v 'libc++'
ldd bin/foobar | grep 'libllvm-unwind.so.1 => /usr/local/lib/libllvm-unwind.so.1'
ldd bin/foobar | grep -v 'libc++abi'
ldd bin/foobar | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1'
ldd bin/foobar | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'

cp -a bin/foobar bin/foobar_cpp_libstdcpp
cp -a bin/foobar_c bin/foobar_c_libstdcpp

conan create /tmp/project/test/clang/conan foo/0.1@user/testing --build -s compiler.libcxx=libstdc++11 -s build_type=Debug
conan install foo/0.1@user/testing -g deploy -s compiler.libcxx=libstdc++11 -s build_type=Debug

bin/foobar_c
bin/foobar

ldd bin/foobar | grep -v 'libc++'
ldd bin/foobar | grep 'libllvm-unwind.so.1 => /usr/local/lib/libllvm-unwind.so.1'
ldd bin/foobar | grep -v 'libc++abi'
ldd bin/foobar | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1'
ldd bin/foobar | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'

cp -a bin/foobar bin/foobar_cpp_libstdcpp11
cp -a bin/foobar_c bin/foobar_c_libstdcpp11

compiler_name=$(conan profile show default | grep -m 1 'compiler' | cut -d "=" -f 2-)
compiler_version=$(conan profile show default | grep 'compiler.version' | cut -d "=" -f 2-)

tar cf "${compiler_name}${compiler_version}.tar" bin/
sudo cp "${compiler_name}${compiler_version}.tar" /tmp/project/
