#!/usr/bin/env bash
sudo docker run -t -d --name clang39 conanio/clang39 && \
sudo docker exec clang39 sudo pip install -U conan_package_tools && \
sudo docker exec clang39 sudo pip install -U conan && \
sudo docker exec clang39 conan user && \
sudo docker exec clang39 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=3.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang39 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=3.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang39 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=3.9 -s compiler.libcxx=libc++ --build && \
sudo docker exec clang39 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=3.9 -s compiler.libcxx=libc++ --build && \
sudo docker stop clang39 && \
sudo docker rm clang39
