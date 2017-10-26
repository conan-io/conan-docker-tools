sudo docker run -t -d --name conangcc71 lasote/conangcc71 && \
sudo docker exec conangcc71 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc71 sudo pip install -U conan && \
sudo docker exec conangcc71 conan user && \
sudo docker exec conangcc71 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=7.1 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc71 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=gcc -s compiler.version=7.1 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc71 && \
sudo docker rm conangcc71
