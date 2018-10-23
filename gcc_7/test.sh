#!/usr/bin/env bash
sudo docker run -t -d --name gcc7 conanio/gcc7 && \
sudo docker exec gcc7 pip install -U conan_package_tools && \
sudo docker exec gcc7 pip install -U conan && \
sudo docker exec gcc7 conan user && \
sudo docker exec gcc7 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=7 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc7 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=7 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc7 && \
sudo docker rm gcc7
