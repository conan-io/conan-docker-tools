#!/usr/bin/env bash
sudo docker run -t -d --name conanclang50 lasote/conanclang50 && \
sudo docker exec conanclang50 sudo pip install -U conan_package_tools && \
sudo docker exec conanclang50 sudo pip install -U conan && \
sudo docker exec conanclang50 conan user && \
sudo docker exec conanclang50 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=clang -s compiler.version=5.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang50 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=clang -s compiler.version=5.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang50 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=clang -s compiler.version=5.0 -s compiler.libcxx=libc++ --build && \
sudo docker exec conanclang50 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=clang -s compiler.version=5.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop conanclang50 && \
sudo docker rm conanclang50
