#!/usr/bin/env bash
sudo docker run -t -d --name gcc48 conanio/gcc48 && \
sudo docker exec gcc48 pip install -U conan_package_tools && \
sudo docker exec gcc48 pip install -U conan && \
sudo docker exec gcc48 conan user && \
sudo docker exec gcc48 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=4.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc48 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=4.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc48 && \
sudo docker rm gcc48
