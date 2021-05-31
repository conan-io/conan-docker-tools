#!/bin/bash

set -ex

PROTOBUF_FOLDER=/home/conan/conan-center-index/recipes/protobuf/all
PROTOBUF_VERSION=3.15.5

export CONAN_PRINT_RUN_COMMANDS=1

if [ ! -d /home/conan/conan-center-index ]; then
    echo "Conan Center Index folder not found. Downloading it now ..."
    git clone https://github.com/conan-io/conan-center-index.git /home/conan/conan-center-index
fi

conan config init --force

conan create ${PROTOBUF_FOLDER} protobuf/${PROTOBUF_VERSION}@ --build -s compiler.libcxx=libstdc++ -s build_type=Release -o protobuf:shared=False

if grep clang /home/conan/.conan/profiles/default ; then
    conan create ${PROTOBUF_FOLDER} protobuf/${PROTOBUF_VERSION}@ --build -s compiler.libcxx=libc++ -s build_type=Release -o protobuf:shared=False
fi