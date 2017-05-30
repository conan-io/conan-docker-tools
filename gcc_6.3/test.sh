#!/bin/bash
sudo docker run --rm lasote/conangcc63 /bin/bash -c "conan user && conan install gtest/1.8.0@lasote/stable -s arch=x86_64 --build && conan install gtest/1.8.0@lasote/stable -s arch=x86 --build"
