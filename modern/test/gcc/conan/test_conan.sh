#!/bin/bash

set -ex

python --version
pip --version
cmake --version
conan --version
cpp --version
cc --version

export CONAN_PRINT_RUN_COMMANDS=1
export CONAN_PRINT_RUN_COMMANDS=1

mkdir -p /tmp/build
rm -rf /tmp/build/*

pushd /tmp/build

conan config init --force
conan install -r conan-center zlib/1.2.11@ --build
conan install -r conan-center spdlog/1.8.5@ --build

conan create /tmp/project/test/gcc/conan foo/0.1@user/testing
conan install foo/0.1@user/testing -g deploy

ldd bin/foobar | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'
ldd bin/foobar | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1'

libstdcpp=$(find /usr/local/lib64 -regex '^\/usr\/local\/lib64\/libstdc\+\+\.so\.6\.0\.[23][0-9]$')

cp "${libstdcpp}" /tmp/build/bin/libstdcpp.so

compiler_name=$(conan profile show default | grep -m 1 'compiler' | cut -d "=" -f 2-)
compiler_version=$(conan profile show default | grep 'compiler.version' | cut -d "=" -f 2-)

tar cf "${compiler_name}${compiler_version}.tar" bin/
sudo cp "${compiler_name}${compiler_version}.tar" /tmp/project/
