#!/usr/bin/env bash
sudo docker run -t -d --name gcc6-armv7hf conanio/gcc8-armv7hf && \
sudo docker exec gcc8-armv7hf sudo pip install -U conan_package_tools && \
sudo docker exec gcc8-armv7hf sudo pip install -U conan && \
sudo docker exec gcc8-armv7hf conan user && \
sudo docker exec gcc8-armv7hf conan install gtest/1.8.0@bincrafters/stable -s arch=armv7hf -s compiler=gcc -s compiler.version=7 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc8-armv7hf && \
sudo docker rm gcc8-armv7hf
