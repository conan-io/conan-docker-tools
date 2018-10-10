#!/usr/bin/env bash
sudo docker run -t -d --name clang7 lasote/clang7 && \
sudo docker exec clang7 sudo pip install -U conan_package_tools && \
sudo docker exec clang7 sudo pip install -U conan && \
sudo docker exec clang7 conan user && \
sudo docker exec clang7 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang7 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec clang7 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libc++ --build && \
sudo docker exec clang7 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=clang -s compiler.version=7.0 -s compiler.libcxx=libc++ --build && \
sudo docker stop clang7 && \
sudo docker rm clang7
