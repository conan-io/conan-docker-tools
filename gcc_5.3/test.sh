#!/bin/bash
sudo docker run --rm lasote/conangcc53 /bin/bash -c "conan user && conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5.3  --build && conan install gtest/1.8.0@lasote/stable -s arch=x86 --build"
