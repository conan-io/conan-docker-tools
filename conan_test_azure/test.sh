#!/usr/bin/env bash
sudo docker run -t -d --name gcc54 conanio/conan_tests_azure && \
sudo docker exec conan_tests_azure sudo pip install -U conan_package_tools && \
sudo docker exec conan_tests_azure sudo pip install -U conan && \
sudo docker exec conan_tests_azure conan user && \
sudo docker exec conan_tests_azure conan install gtest/1.8.0@conanio/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conan_tests_azure conan install gtest/1.8.0@conanio/stable -s arch=x86 -s compiler=gcc -s compiler.version=5.4 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conan_tests_azure && \
sudo docker rm conan_tests_azure
