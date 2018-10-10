#!/usr/bin/env bash
sudo docker run -t -d --name clang70-x86 conanio/clang70-x86 && \
sudo docker exec clang70-x86 sudo pip install -U conan_package_tools && \
sudo docker exec clang70-x86 sudo pip install -U conan && \
sudo docker exec clang70-x86 conan user && \
sudo docker exec clang70-x86 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang70-x86 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop clang70-x86 && \
sudo docker rm clang70-x86
