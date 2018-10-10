#!/usr/bin/env bash
sudo docker run -t -d --name conangcc7 conanio/conangcc7 && \
sudo docker exec conangcc7 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc7 sudo pip install -U conan && \
sudo docker exec conangcc7 conan user && \
sudo docker exec conangcc7 conan install gtest/1.8.0@conanio/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=7 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc7 conan install gtest/1.8.0@conanio/stable -s arch=x86 -s compiler=gcc -s compiler.version=7 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc7 && \
sudo docker rm conangcc7
