#!/bin/bash

set -ex

compiler=$1
container="$compiler-"$(openssl rand -hex 2)

docker run -t -d -v ${PWD}:/tmp/project --name ${container} ${DOCKER_USERNAME}/${compiler}-ubuntu16.04
docker exec ${container} git clone https://github.com/conan-io/conan-center-index.git
docker exec ${container} /tmp/project/test/standard/build_imagl.sh
docker exec ${compcontaineriler} /tmp/project/test/standard/build_libsolace.sh

docker stop ${container}
docker rm -f ${container}
