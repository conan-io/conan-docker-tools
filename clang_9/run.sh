#!/usr/bin/env bash
sudo docker run --rm -v ~/.conan/data:/home/conan/.conan/data -it conanio/clang9 /bin/bash
