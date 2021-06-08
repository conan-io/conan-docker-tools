#!/bin/bash

set -ex

LIBSOLACE_FOLDER=/home/conan/conan-center-index/recipes/libsolace/all
LIBSOLACE_VERSION=0.3.9

export CONAN_PRINT_RUN_COMMANDS=1

conan config init --force

if [ ! -d /home/conan/conan-center-index ]; then
    echo "Conan Center Index folder not found. Downloading it now ..."
    git clone https://github.com/conan-io/conan-center-index.git /home/conan/conan-center-index
fi

echo "Building libsolace ${LIBSOLACE_VERSION} - Requires C++17"

if grep gcc /home/conan/.conan/profiles/default ; then
    if egrep 'compiler\.version=(8|9|10|11|12)' /home/conan/.conan/profiles/default; then
        conan create ${LIBSOLACE_FOLDER} ${LIBSOLACE_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release
        conan create ${LIBSOLACE_FOLDER} ${LIBSOLACE_VERSION}@ --build -s compiler.libcxx=libstdc++11 -s build_type=Release

        conan create ${LIBSOLACE_FOLDER} ${LIBSOLACE_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release -o libsolace:shared=True
        conan install libsolace/${LIBSOLACE_VERSION}@ -g deploy -s compiler.libcxx=libstdc++ -s build_type=Release -o libsolace:shared=True
        ldd libsolace/lib/libsolace.so | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'
        ldd libsolace/lib/libsolace.so | grep 'libc.so.6 => /lib/x86_64-linux-gnu/libc.so'
    fi
elif grep clang /home/conan/.conan/profiles/default ; then
    conan create ${LIBSOLACE_FOLDER} ${LIBSOLACE_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release
    conan create ${LIBSOLACE_FOLDER} ${LIBSOLACE_VERSION}@ --build -s compiler.libcxx=libstdc++11 -s build_type=Release
    conan create ${LIBSOLACE_FOLDER} ${LIBSOLACE_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release

    conan create ${LIBSOLACE_FOLDER} ${LIBSOLACE_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release -o libsolace:shared=True
    conan install libsolace/${LIBSOLACE_VERSION}@ -g deploy -s compiler.libcxx=libc++ -s build_type=Release -o libsolace:shared=True
    ldd libsolace/lib/libsolace.so | grep 'libc++.so.1 => /usr/local/lib/libc++.so.1'
fi