#!/usr/bin/env bash
sudo docker run -t -d --name conangcc6-x86 conanio/conangcc6-x86 && \
sudo docker exec conangcc6-x86 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc6-x86 sudo pip install -U conan && \
sudo docker exec conangcc6-x86 conan user && \
sudo docker exec conangcc6-x86 conan install gtest/1.8.0@conanio/stable -s arch=x86 -s compiler=gcc -s compiler.version=6 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc6-x86 && \
sudo docker rm conangcc6
