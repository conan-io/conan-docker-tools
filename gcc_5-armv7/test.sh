#!/usr/bin/env bash
sudo docker run -t -d --name conangcc5-armv7 lasote/conangcc5-armv7 && \
sudo docker exec conangcc5-armv7 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc5-armv7 sudo pip install -U conan && \
sudo docker exec conangcc5-armv7 conan user && \
sudo docker exec conangcc5-armv7 conan install gtest/1.8.1@bincrafters/stable -s arch=armv7 -s compiler=gcc -s compiler.version=5 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc5-armv7 && \
sudo docker rm conangcc5-armv7
