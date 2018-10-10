#!/usr/bin/env bash
sudo docker run --rm -v ~/.conan/data:/home/conan/.conan/data -it conanio/gcc7-armv7 /bin/bash
