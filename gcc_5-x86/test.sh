#!/usr/bin/env bash
sudo docker run -t -d --name conangcc5-x86 lasote/conangcc5-x86 && \
sudo docker exec conangcc5-x86 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc5-x86 sudo pip install -U conan && \
sudo docker exec conangcc5-x86 conan user && \
sudo docker exec conangcc5-x86 conan install gtest/1.8.0@conan/stable -s arch=x86 -s compiler=gcc -s compiler.version=5 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc5-x86 && \
sudo docker rm conangcc5-x86
