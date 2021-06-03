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

conan create ../project/test/clang/conan foo/0.1@user/testing --build -s compiler.libcxx=libc++
conan install foo/0.1@user/testing -g deploy -s compiler.libcxx=libc++

ldd bin/foobar | grep 'libc++.so.1 => /usr/local/lib/libc++.so.1'
ldd bin/foobar | grep 'libllvm-unwind.so.1 => /usr/local/lib/libllvm-unwind.so.1'
ldd bin/foobar | grep -v 'libgcc'

sudo mv bin/foobar ../project/foobar_cpp_libcpp
sudo mv bin/foobar_c ../project/foobar_c_libcpp

sudo cp /usr/local/lib64/libstdc++.so.6.0.29 ../project/libstdc++.so.6.0.29
sudo cp /usr/local/lib64/libatomic.so.1.2.0 ../project/libatomic.so.1.2.0
sudo cp /usr/local/lib/libllvm-unwind.so.1.0 ../project/libllvm-unwind.so.1.0

sudo cp /usr/local/lib/libllvm-unwind.so.1.0 ../project/libunwind.so.1.0
sudo cp /usr/local/lib/libc++.so.1.0 ../project/libc++.so.1.0
sudo cp /usr/local/lib/libc++abi.so.1.0 ../project/libc++abi.so.1.0

conan create ../project/test/clang/conan foo/0.1@user/testing --build -s compiler.libcxx=libstdc++
conan install foo/0.1@user/testing -g deploy -s compiler.libcxx=libstdc++

ldd bin/foobar | grep -v 'libc++'
ldd bin/foobar | grep 'libllvm-unwind.so.1 => /usr/local/lib/libllvm-unwind.so.1'
ldd bin/foobar | grep -v 'libc++abi'
ldd bin/foobar | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1'
ldd bin/foobar | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'

sudo cp -a bin/foobar ../project/foobar_cpp_libstdcpp
sudo cp -a bin/foobar_c ../project/foobar_c_libstdcpp

conan create ../project/test/clang/conan foo/0.1@user/testing --build -s compiler.libcxx=libstdc++11
conan install foo/0.1@user/testing -g deploy -s compiler.libcxx=libstdc++11

ldd bin/foobar | grep -v 'libc++'
ldd bin/foobar | grep 'libllvm-unwind.so.1 => /usr/local/lib/libllvm-unwind.so.1'
ldd bin/foobar | grep -v 'libc++abi'
ldd bin/foobar | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1'
ldd bin/foobar | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'

sudo cp -a bin/foobar /tmp/project/foobar_cpp_libstdcpp11
sudo cp -a bin/foobar_c /tmp/project/foobar_c_libstdcpp11
