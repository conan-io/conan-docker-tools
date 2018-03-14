#!/usr/bin/env bash
sudo docker run -t -d --name conangcc49-armv7hf lasote/conangcc49-armv7hf && \
sudo docker exec conangcc49-armv7hf sudo pip install -U conan_package_tools && \
sudo docker exec conangcc49-armv7hf sudo pip install -U conan && \
sudo docker exec conangcc49-armv7hf conan user && \
sudo docker exec conangcc49-armv7hf conan install gtest/1.8.0@lasote/stable -s arch=armv7hf -s compiler=gcc -s compiler.version=4.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc49-armv7hf && \
sudo docker rm conangcc49-armv7hf
