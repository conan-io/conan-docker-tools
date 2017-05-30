#!/bin/bash
sudo docker run --rm lasote/conangcc46 /bin/bash -c "conan user && conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=4.6 --build && conan install gtest/1.8.0@lasote/stable -s arch=x86 --build"
