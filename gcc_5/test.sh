#!/usr/bin/env bash
sudo docker run -t -d --name gcc5 conanio/gcc5 && \
sudo docker exec gcc5 sudo pip install -U conan_package_tools && \
sudo docker exec gcc5 sudo pip install -U conan && \
sudo docker exec gcc5 conan user && \
sudo docker exec gcc5 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc5 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=5 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc5 && \
sudo docker rm gcc5
