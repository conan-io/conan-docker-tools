#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    brew update || brew update
    brew outdated pyenv || brew upgrade pyenv
    brew install pyenv-virtualenv
    brew unlink cmake
    brew upgrade cmake
    brew install gcc || brew link --overwrite gcc
    brew install ninja
    brew install conan
    conan user
fi
