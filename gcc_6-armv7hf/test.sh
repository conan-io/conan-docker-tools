#!/usr/bin/env bash
sudo docker run -t -d --name gcc6-armv7hf conanio/gcc6-armv7hf && \
sudo docker exec gcc6-armv7hf sudo pip install -U conan_package_tools && \
sudo docker exec gcc6-armv7hf sudo pip install -U conan && \
sudo docker exec gcc6-armv7hf conan user && \
sudo docker exec gcc6-armv7hf conan install gtest/1.8.0@conanio/stable -s arch=armv7hf -s compiler=gcc -s compiler.version=6 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc6-armv7hf && \
sudo docker rm gcc6-armv7hf
