#!/usr/bin/env bash
sudo docker run -t -d --name conangcc54 conanio/conangcc54 && \
sudo docker exec conangcc54 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc54 sudo pip install -U conan && \
sudo docker exec conangcc54 conan user && \
sudo docker exec conangcc54 conan install gtest/1.8.0@conanio/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc54 conan install gtest/1.8.0@conanio/stable -s arch=x86 -s compiler=gcc -s compiler.version=5.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc54 && \
sudo docker rm conangcc54
