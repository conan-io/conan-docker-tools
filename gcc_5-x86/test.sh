#!/usr/bin/env bash
sudo docker run -t -d --name gcc5-x86 conanio/gcc5-x86 && \
sudo docker exec gcc5-x86 sudo pip install -U conan_package_tools && \
sudo docker exec gcc5-x86 sudo pip install -U conan && \
sudo docker exec gcc5-x86 conan user && \
sudo docker exec gcc5-x86 conan install gtest/1.8.1@conan/stable -s arch=x86 -s compiler=gcc -s compiler.version=5 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc5-x86 && \
sudo docker rm gcc5-x86
