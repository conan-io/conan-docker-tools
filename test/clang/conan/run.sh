#!/bin/bash

set -ex

compiler=$1
container="$compiler-"$(openssl rand -hex 2)

docker pull ${DOCKER_USERNAME}/${compiler}-ubuntu16.04
docker run -t -d -v ${PWD}:/tmp/project --name ${container} ${DOCKER_USERNAME}/${compiler}-ubuntu16.04
docker exec ${container} /tmp/project/test/clang/conan/test_conan.sh

docker stop ${container}
docker rm -f ${container}

# Mount Vanilla Ubuntu Xenial and run executables built with libstdc++.so.0.6.28
container="ubuntu-"$(openssl rand -hex 2)
docker run -t -d -v ${PWD}:/tmp/project --name ${container} ubuntu:xenial

docker exec -w /tmp/project ${container} cp libllvm-unwind.so.1.0 /usr/lib/x86_64-linux-gnu/libllvm-unwind.so.1
docker exec -w /tmp/project ${container} cp libllvm-unwind.so.1.0 /usr/lib/x86_64-linux-gnu/libunwind.so.1
docker exec -w /tmp/project ${container} cp libc++.so.1.0 /usr/lib/x86_64-linux-gnu/libc++.so.1
docker exec -w /tmp/project ${container} cp libc++abi.so.1.0 /usr/lib/x86_64-linux-gnu/libc++abi.so.1
docker exec -w /tmp/project ${container} cp libstdc++.so.6.0.28 /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.21
docker exec -w /tmp/project ${container} cp libatomic.so.1.2.0 /usr/lib/x86_64-linux-gnu/libatomic.so.1

docker exec -w /tmp/project ${container} ./foobar_cpp_libcpp
docker exec -w /tmp/project ${container} ./foobar_c_libcpp

docker exec -w /tmp/project ${container} ./foobar_cpp_libstdcpp
docker exec -w /tmp/project ${container} ./foobar_c_libstdcpp

docker exec -w /tmp/project ${container} ./foobar_cpp_libstdcpp11
docker exec -w /tmp/project ${container} ./foobar_c_libstdcpp11

docker stop ${container}
docker rm -f ${container}
