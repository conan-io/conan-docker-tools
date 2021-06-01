#!/bin/bash

set -ex

compiler=$1
container="$compiler-"$(openssl rand -hex 2)

docker run -t -d -v ${PWD}:/tmp/project --name ${container} ${DOCKER_USERNAME}/${compiler}-ubuntu16.04
docker exec ${container} /tmp/project/test/gcc/fortran/test_fortran.sh

docker stop ${container}
docker rm -f ${container}
