#!/usr/bin/env bash
sudo docker run -t -d --name clang38 conanio/clang38 && \
sudo docker exec clang38 pip install -U conan_package_tools && \
sudo docker exec clang38 pip install -U conan && \
sudo docker exec clang38 conan user && \
sudo docker exec clang38 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang38 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang38 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libc++ --build && \
sudo docker exec clang38 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=3.8 -s compiler.libcxx=libc++ --build && \
sudo docker stop clang38 && \
sudo docker rm clang38
