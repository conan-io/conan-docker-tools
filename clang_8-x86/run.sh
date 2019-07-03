#!/usr/bin/env bash
sudo docker run --rm -v ~/.conan/data:/root/.conan/data -it conanio/clang8-x86 /bin/bash
