#!/usr/bin/env bash
sudo docker run -t -d --name conangcc6-armv7hf lasote/conangcc6-armv7hf && \
sudo docker exec conangcc6-armv7hf sudo pip install -U conan_package_tools && \
sudo docker exec conangcc6-armv7hf sudo pip install -U conan && \
sudo docker exec conangcc6-armv7hf conan user && \
sudo docker exec conangcc6-armv7hf conan install gtest/1.8.0@lasote/stable -s arch=armv7hf -s compiler=gcc -s compiler.version=6 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc6-armv7hf && \
sudo docker rm conangcc6-armv7hf
