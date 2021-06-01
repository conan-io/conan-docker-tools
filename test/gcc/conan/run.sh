#!/bin/bash

set -ex

compiler=$1
container="$compiler-"$(openssl rand -hex 2)

docker pull ${DOCKER_USERNAME}/${compiler}-ubuntu16.04
docker run -t -d -v ${PWD}:/tmp/project --name ${container} ${DOCKER_USERNAME}/${compiler}-ubuntu16.04
docker exec ${container} /tmp/project/test/gcc/conan/test_conan.sh

docker stop ${container}
docker rm -f ${container}

container="ubuntu-"$(openssl rand -hex 2)

# Mount Vanilla Ubuntu Xenial and run executables built with libstdc++.so.0.6.28
docker run -t -d -v ${PWD}:/tmp/project --name ${container} ubuntu:xenial
# Default Xenial libstdc++ is too old, foobar requires GLIBCXX_3.4.22
docker exec -w /tmp/project ${container} cp libstdc++.so.6.0.28 /usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.21
docker exec -w /tmp/project ${container} ./foobar
# No big deal with C app. It requires only libc
docker exec -w /tmp/project ${container} ./foobar_c

docker stop ${container}
docker rm -f ${container}
