#!/usr/bin/env bash
sudo docker run -t -d --name conanclang7-x86 lasote/conanclang7-x86 && \
sudo docker exec conanclang7-x86 sudo pip install -U conan_package_tools && \
sudo docker exec conanclang7-x86 sudo pip install -U conan && \
sudo docker exec conanclang7-x86 conan user && \
sudo docker exec conanclang7-x86 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang7-x86 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop conanclang7-x86 && \
sudo docker rm conanclang7-x86
