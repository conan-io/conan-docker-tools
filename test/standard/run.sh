#!/bin/bash

set -ex

compiler=$1

docker run -t -d -v ${PWD}:/tmp/project --name ${compiler} ${DOCKER_USERNAME}/${compiler}-ubuntu16.04
docker exec ${compiler} git clone https://github.com/conan-io/conan-center-index.git
docker exec ${compiler} /tmp/project/test/standard/build_imagl.sh
docker exec ${compiler} /tmp/project/test/standard/build_libsolace.sh

docker stop ${compiler}
docker rm -f ${compiler}
