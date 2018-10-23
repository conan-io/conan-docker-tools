#!/usr/bin/env bash
sudo docker run -t -d --name clang40 conanio/clang40 && \
sudo docker exec clang40 pip install -U conan_package_tools && \
sudo docker exec clang40 pip install -U conan && \
sudo docker exec clang40 conan user && \
sudo docker exec clang40 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=4.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang40 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=4.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang40 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=4.0 -s compiler.libcxx=libc++ --build && \
sudo docker exec clang40 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=4.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop clang40 && \
sudo docker rm clang40
