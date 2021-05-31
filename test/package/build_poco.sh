#!/bin/bash

set -ex

POCO_FOLDER=/home/conan/conan-center-index/recipes/poco/all
POCO_VERSION=1.9.4

export CONAN_PRINT_RUN_COMMANDS=1

if [ ! -d /home/conan/conan-center-index ]; then
    echo "Conan Center Index folder not found. Downloading it now ..."
    git clone https://github.com/conan-io/conan-center-index.git /home/conan/conan-center-index
fi

conan config init --force

conan create ${POCO_FOLDER} poco/${POCO_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release -o poco:shared=False

if grep clang /home/conan/.conan/profiles/default ; then
    conan create ${POCO_FOLDER} poco/${POCO_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release -o poco:shared=False
fi