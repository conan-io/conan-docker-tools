#!/bin/bash

set -ex

IMAGL_FOLDER=/home/conan/conan-center-index/recipes/imagl/all
IMAGL_VERSION=0.2.1

export CONAN_PRINT_RUN_COMMANDS=1

if [ ! -d /home/conan/conan-center-index ]; then
    echo "Conan Center Index folder not found. Downloading it now ..."
    git clone https://github.com/conan-io/conan-center-index.git /home/conan/conan-center-index
fi


echo "Building Imagl ${IMAGL_VERSION} - Requires C++20"

conan config init --force

if grep clang /home/conan/.conan/profiles/default ; then
    if grep compiler.version=10 /home/conan/.conan/profiles/default ; then
        conan create ${IMAGL_FOLDER} ${IMAGL_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release
        conan create ${IMAGL_FOLDER} ${IMAGL_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release -o imagl:shared=True
        conan install imagl/${IMAGL_VERSION}@ -g deploy -s compiler.libcxx=libc++ -s build_type=Release -o imagl:shared=True
        ldd imagl/lib/libimaGL.so | grep 'libc++.so.1 => /usr/local/lib/libc++.so.1'
    fi
elif egrep 'compiler\.version=(9|10|11|12)' /home/conan/.conan/profiles/default; then
    conan create ${IMAGL_FOLDER} ${IMAGL_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release
    conan create ${IMAGL_FOLDER} ${IMAGL_VERSION}@ --build -s compiler.libcxx=libstdc++11 -s build_type=Release -o imagl:shared=True
    conan install imagl/${IMAGL_VERSION}@ -g deploy -s compiler.libcxx=libstdc++11 -s build_type=Release -o imagl:shared=True
    ldd imagl/lib/libimaGL.so | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'
    ldd imagl/lib/libimaGL.so | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so'

fi
