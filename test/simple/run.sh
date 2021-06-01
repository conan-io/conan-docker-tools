#!/bin/bash

set -ex

compiler=$1
container="$compiler-"$(openssl rand -hex 2)

docker rm -f ${compiler}

docker run -t -d -v ${PWD}:/tmp/project --name ${container} ${DOCKER_USERNAME}/${compiler}
docker exec ${container} /tmp/project/test/simple/test_simple.sh

docker stop ${container}
docker rm -f ${container}
