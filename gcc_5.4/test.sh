#!/usr/bin/env bash
sudo docker run -t -d --name gcc54 conanio/gcc54 && \
sudo docker exec gcc54 pip install -U conan_package_tools && \
sudo docker exec gcc54 pip install -U conan && \
sudo docker exec gcc54 conan user && \
sudo docker exec gcc54 conan install gtest/1.8.0@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc54 conan install gtest/1.8.0@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=5.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc54 && \
sudo docker rm gcc54
