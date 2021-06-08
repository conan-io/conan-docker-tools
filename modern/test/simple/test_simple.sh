#!/bin/bash

set -ex

mkdir -p /tmp/build
rm -rf /tmp/build/*

pushd /tmp/build

cmake ../project/test/simple -DCMAKE_BUILD_TYPE=Release
cmake --build .

./example-c
./example-cpp

if [ -f /usr/local/bin/clang ]; then
    ./example-c-clang
    ./example-cpp-clang
fi