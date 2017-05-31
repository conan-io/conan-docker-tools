sudo docker run -t -d --name conangcc49 lasote/conangcc49 && \
sudo docker exec conangcc49 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc49 sudo pip install -U conan && \
sudo docker exec conangcc49 conan user && \
sudo docker exec conangcc49 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=5.2 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc49 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=gcc -s compiler.version=5.2 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc49 && \
sudo docker rm conangcc49
