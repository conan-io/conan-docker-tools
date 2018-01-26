#!/usr/bin/env bash
sudo docker run -t -d --name conangcc64 lasote/conangcc64 && \
sudo docker exec conangcc64 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc64 sudo pip install -U conan && \
sudo docker exec conangcc64 conan user && \
sudo docker exec conangcc64 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=6.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc64 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=gcc -s compiler.version=6.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc64 && \
sudo docker rm conangcc64
