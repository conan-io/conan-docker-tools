#!/usr/bin/env bash
sudo docker run -t -d --name conanclang60-x86 conanio/conanclang60-x86 && \
sudo docker exec conanclang60-x86 sudo pip install -U conan_package_tools && \
sudo docker exec conanclang60-x86 sudo pip install -U conan && \
sudo docker exec conanclang60-x86 conan user && \
sudo docker exec conanclang60-x86 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=6.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang60-x86 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=6.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop conanclang60-x86 && \
sudo docker rm conanclang60-x86
