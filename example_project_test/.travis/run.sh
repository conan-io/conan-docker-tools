#!/bin/bash

if [[ "$(uname -s)" == 'Darwin' ]]; then
    # Run with native OSX
    ./run_project_build.sh
else
    # Run with docker
    if [ -z ${GCC_VERSION+x} ]; then
        docker run -v$(pwd):/home/conan lasote/conangcc$GCC_VERSION "./run_project_build.sh"
    fi

    if [ -z ${CLANG_VERSION+x} ]; then
        docker run -v$(pwd):/home/conan lasote/conanclang$CLANG_VERSION "./run_project_build.sh"
    fi
fi