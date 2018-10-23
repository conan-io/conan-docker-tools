#!/usr/bin/env bash
sudo docker run -t -d --name clang7-x86 conanio/clang7-x86 && \
sudo docker exec clang7-x86 pip install -U conan_package_tools && \
sudo docker exec clang7-x86 pip install -U conan && \
sudo docker exec clang7-x86 conan user && \
sudo docker exec clang7-x86 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang7-x86 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop clang7-x86 && \
sudo docker rm clang7-x86
