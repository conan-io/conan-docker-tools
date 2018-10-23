#!/usr/bin/env bash
sudo docker run -t -d --name gcc64 conanio/gcc64 && \
sudo docker exec gcc64 pip install -U conan_package_tools && \
sudo docker exec gcc64 pip install -U conan && \
sudo docker exec gcc64 conan user && \
sudo docker exec gcc64 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=6.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc64 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=6.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc64 && \
sudo docker rm gcc64
