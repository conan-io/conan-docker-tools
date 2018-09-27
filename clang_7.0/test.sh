#!/usr/bin/env bash
sudo docker run -t -d --name conanclang70 lasote/conanclang70 && \
sudo docker exec conanclang70 sudo pip install -U conan_package_tools && \
sudo docker exec conanclang70 sudo pip install -U conan && \
sudo docker exec conanclang70 conan user && \
sudo docker exec conanclang70 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang70 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang70 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libc++ --build && \
sudo docker exec conanclang70 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop conanclang70 && \
sudo docker rm conanclang70
