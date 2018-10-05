#!/usr/bin/env bash
sudo docker run -t -d --name conangcc48 lasote/conangcc48 && \
sudo docker exec conangcc48 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc48 sudo pip install -U conan && \
sudo docker exec conangcc48 conan user && \
sudo docker exec conangcc48 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=4.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc48 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=4.8 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc48 && \
sudo docker rm conangcc48
