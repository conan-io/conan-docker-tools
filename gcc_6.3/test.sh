sudo docker run -t -d --name conangcc63 lasote/conangcc63 && \
sudo docker exec conangcc63 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc63 sudo pip install -U conan && \
sudo docker exec conangcc63 conan user && \
sudo docker exec conangcc63 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=6.3 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc63 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=gcc -s compiler.version=6.3 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc63 && \
sudo docker rm conangcc63
