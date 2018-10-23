#!/usr/bin/env bash
sudo docker run -t -d --name gcc49-armv7 conanio/gcc49-armv7 && \
sudo docker exec gcc49-armv7 pip install -U conan_package_tools && \
sudo docker exec gcc49-armv7 pip install -U conan && \
sudo docker exec gcc49-armv7 conan user && \
sudo docker exec gcc49-armv7 conan install gtest/1.8.1@bincrafters/stable -s arch=armv7 -s compiler=gcc -s compiler.version=4.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc49-armv7 && \
sudo docker rm gcc49-armv7
