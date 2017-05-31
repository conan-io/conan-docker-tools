#!/bin/bash
sudo docker run --rm lasote/conangcc63 /bin/bash -c "sudo pip install conan-package_tools --upgrade && sudo pip install conan --upgrade && conan user && conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=6.3 --build && conan install gtest/1.8.0@lasote/stable -s arch=x86 --build"
