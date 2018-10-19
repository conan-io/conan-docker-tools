#!/usr/bin/env bash
sudo docker run -t -d --name gcc49-x86 conanio/gcc49-x86 && \
sudo docker exec gcc49-x86 sudo pip install -U conan_package_tools && \
sudo docker exec gcc49-x86 sudo pip install -U conan && \
sudo docker exec gcc49-x86 conan user && \
sudo docker exec gcc49-x86 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=4.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc49-x86 && \
sudo docker rm gcc49-x86
