#!/usr/bin/env bash
sudo docker run -t -d --name gcc53 conanio/gcc53 && \
sudo docker exec gcc53 sudo pip install -U conan_package_tools && \
sudo docker exec gcc53 sudo pip install -U conan && \
sudo docker exec gcc53 conan user && \
sudo docker exec gcc53 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5.3 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc53 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=5.3 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc53 && \
sudo docker rm gcc53
