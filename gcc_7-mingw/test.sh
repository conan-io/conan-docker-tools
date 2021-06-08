#!/usr/bin/env bash
sudo docker run -t -d --name conangcc7-mingw lasote/conangcc7-mingw && \
sudo docker exec conangcc7-mingw sudo pip install -U conan_package_tools && \
sudo docker exec conangcc7-mingw sudo pip install -U conan && \
sudo docker exec conangcc7-mingw conan user && \
sudo docker exec conangcc7-mingw conan install zlib/1.2.11@conan/stable -s os=Windows -s arch=x86_64 -s compiler=gcc -s compiler.version=7 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc7-mingw && \
sudo docker rm conangcc7-mingw
