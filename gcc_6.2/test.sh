#!/usr/bin/env bash
sudo docker run -t -d --name conangcc62 lasote/conangcc62 && \
sudo docker exec conangcc62 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc62 sudo pip install -U conan && \
sudo docker exec conangcc62 conan user && \
sudo docker exec conangcc62 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=6.2 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc62 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=gcc -s compiler.version=6.2 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc62 && \
sudo docker rm conangcc62
