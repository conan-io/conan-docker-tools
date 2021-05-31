#!/bin/bash

set -ex

mkdir -p /tmp/build
rm -rf /tmp/build/*

pushd /tmp/build

which gfortran
gfortran --version

cmake ../project/test/gcc/fortran -DCMAKE_BUILD_TYPE=Release
cmake --build .

./hello
