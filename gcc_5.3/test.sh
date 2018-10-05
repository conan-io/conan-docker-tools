#!/usr/bin/env bash
sudo docker run -t -d --name conangcc53 lasote/conangcc53 && \
sudo docker exec conangcc53 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc53 sudo pip install -U conan && \
sudo docker exec conangcc53 conan user && \
sudo docker exec conangcc53 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5.3 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc53 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=5.3 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc53 && \
sudo docker rm conangcc53
