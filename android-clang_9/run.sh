#!/usr/bin/env bash
docker run --rm -v ~/.conan/data:/home/conan/.conan/data -it conanio/android-clang9 /bin/bash
