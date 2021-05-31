#!/bin/bash

set -ex

GTEST_FOLDER=/home/conan/conan-center-index/recipes/gtest/all
GTEST_VERSION=1.8.1

export CONAN_PRINT_RUN_COMMANDS=1

if [ ! -d /home/conan/conan-center-index ]; then
    echo "Conan Center Index folder not found. Downloading it now ..."
    git clone https://github.com/conan-io/conan-center-index.git /home/conan/conan-center-index
fi

conan config init --force

conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release -o gtest:shared=False
conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Debug   -o gtest:shared=False
conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release -o gtest:shared=True
conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Debug   -o gtest:shared=True

conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++11 -s build_type=Release -o gtest:shared=False
conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++11 -s build_type=Debug   -o gtest:shared=False
conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++11 -s build_type=Release -o gtest:shared=True
conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libstdc++11 -s build_type=Debug   -o gtest:shared=True

if grep clang /home/conan/.conan/profiles/default ; then
    conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release -o gtest:shared=False
    conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Debug   -o gtest:shared=False
    conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release -o gtest:shared=True
    conan create ${GTEST_FOLDER} gtest/${GTEST_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Debug   -o gtest:shared=True
fi