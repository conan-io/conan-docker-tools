#!/usr/bin/env bash
sudo docker run --rm -v ~/.conan/data:/root/.conan/data -it conanio/android-clang8 /bin/bash
