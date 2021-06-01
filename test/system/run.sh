#!/bin/bash

set -ex

compiler=$1
container="$compiler-"$(openssl rand -hex 2)

docker pull ${DOCKER_USERNAME}/${compiler}
docker run -t -d -v ${PWD}:/tmp/project --name ${container} ${DOCKER_USERNAME}/${compiler}-ubuntu16.04

docker exec ${container} conan config init --force
docker exec ${container} conan config set general.sysrequires_mode=enabled

docker exec ${container} sudo cp /tmp/project/test/system/sources.list /etc/apt/sources.list
docker exec ${container} sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60C317803A41BA51845E371A1E9377A2BA9EF27F
docker exec ${container} sudo apt-get -qq update
docker exec ${container} sudo apt-get -qq install -y --force-yes --no-install-recommends --no-install-suggests -o=Dpkg::Use-Pty=0 g++-9

docker exec ${container} mkdir /tmp/build
docker exec -w /tmp/build ${container} conan install ../project/test/system --build
docker exec -w /tmp/build ${container} cmake ../project/test/system -DCMAKE_BUILD_TYPE=Release
docker exec -w /tmp/build ${container} cmake --build .
docker exec -w /tmp/build ${container} ldd bin/package_test
docker exec -w /tmp/build ${container} ldd bin/package_test | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'
docker exec -w /tmp/build ${container} ldd bin/package_test | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1'

docker stop ${container}
docker rm -f ${container}
