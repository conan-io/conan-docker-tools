#!/usr/bin/env bash
sudo docker run -t -d --name clang60 conanio/clang60 && \
sudo docker exec clang60 pip install -U conan_package_tools && \
sudo docker exec clang60 pip install -U conan && \
sudo docker exec clang60 conan user && \
sudo docker exec clang60 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=6.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang60 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=6.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang60 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=6.0 -s compiler.libcxx=libc++ --build && \
sudo docker exec clang60 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=6.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop clang60 && \
sudo docker rm clang60
