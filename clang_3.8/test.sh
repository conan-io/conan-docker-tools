#!/usr/bin/env bash
sudo docker run -t -d --name conanclang38 lasote/conanclang38 && \
sudo docker exec conanclang38 sudo pip install -U conan_package_tools && \
sudo docker exec conanclang38 sudo pip install -U conan && \
sudo docker exec conanclang38 conan user && \
sudo docker exec conanclang38 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang38 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang38 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libc++ --build && \
sudo docker exec conanclang38 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libc++ --build && \
sudo docker stop conanclang38 && \
sudo docker rm conanclang38
