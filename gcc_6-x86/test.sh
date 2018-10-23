#!/usr/bin/env bash
sudo docker run -t -d --name gcc6-x86 conanio/gcc6-x86 && \
sudo docker exec gcc6-x86 pip install -U conan_package_tools && \
sudo docker exec gcc6-x86 pip install -U conan && \
sudo docker exec gcc6-x86 conan user && \
sudo docker exec gcc6-x86 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=6 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc6-x86 && \
sudo docker rm gcc6
