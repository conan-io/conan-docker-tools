#!/usr/bin/env bash
sudo docker run -t -d --name gcc46 conanio/gcc46 && \
sudo docker exec gcc46 pip install -U conan_package_tools && \
sudo docker exec gcc46 pip install -U conan && \
sudo docker exec gcc46 conan user && \
sudo docker exec gcc46 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=4.6 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec gcc46 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler=gcc -s compiler.version=4.6 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop gcc46 && \
sudo docker rm gcc46
