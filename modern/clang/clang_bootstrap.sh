#!/bin/bash

set -ex

version=`conan --version | awk '{print $3}'`


if [[ "${version}" == 2.* ]]
then
    conan profile detect
else
    conan profile new --detect --force default 
fi
