#!/usr/bin/env bash
sudo docker run -t -d --name gcc62 conanio/gcc62 && \
sudo docker exec gcc62 sudo pip install -U conan_package_tools && \
sudo docker exec gcc62 sudo pip install -U conan && \
sudo docker exec gcc62 conan user && \
sudo docker exec gcc62 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=6.2 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc62 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=6.2 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc62 && \
sudo docker rm gcc62
