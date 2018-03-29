#!/usr/bin/env bash
sudo docker run -t -d --name conangcc49-x86 lasote/conangcc49-x86 && \
sudo docker exec conangcc49-x86 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc49-x86 sudo pip install -U conan && \
sudo docker exec conangcc49-x86 conan user && \
sudo docker exec conangcc49-x86 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=gcc -s compiler.version=4.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc49-x86 && \
sudo docker rm conangcc49-x86
