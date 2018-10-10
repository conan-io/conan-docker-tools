#!/usr/bin/env bash
sudo docker run -t -d --name gcc7-x86 conanio/gcc7-x86 && \
sudo docker exec gcc7-x86 sudo pip install -U conan_package_tools && \
sudo docker exec gcc7-x86 sudo pip install -U conan && \
sudo docker exec gcc7-x86 conan user && \
sudo docker exec gcc7-x86 conan install gtest/1.8.0@conanio/stable -s arch=x86 -s compiler=gcc -s compiler.version=7 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc7-x86 && \
sudo docker rm gcc7-x86
