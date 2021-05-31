#!/bin/bash

set -ex

compiler=$1

docker rm -f ${compiler}

docker pull ${DOCKER_USERNAME}/${compiler}
docker run -t -d -v ${PWD}:/tmp/project --name ${compiler} ${DOCKER_USERNAME}/${compiler}-ubuntu16.04

docker exec ${compiler} conan config init --force
docker exec ${compiler} conan config set general.sysrequires_mode=enabled

docker exec ${compiler} sudo cp /tmp/project/test/system/sources.list /etc/apt/sources.list
docker exec ${compiler} sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60C317803A41BA51845E371A1E9377A2BA9EF27F
docker exec ${compiler} sudo apt-get -qq update
docker exec ${compiler} sudo apt-get -qq install -y --force-yes --no-install-recommends --no-install-suggests -o=Dpkg::Use-Pty=0 g++-9

docker exec ${compiler} mkdir /tmp/build
docker exec -w /tmp/build ${compiler} conan install ../project/test/system --build
docker exec -w /tmp/build ${compiler} cmake ../project/test/system -DCMAKE_BUILD_TYPE=Release
docker exec -w /tmp/build ${compiler} cmake --build .
docker exec -w /tmp/build ${compiler} ldd bin/package_test
docker exec -w /tmp/build ${compiler} ldd bin/package_test | grep 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6'
docker exec -w /tmp/build ${compiler} ldd bin/package_test | grep 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1'

docker stop ${compiler}
docker rm ${compiler}
