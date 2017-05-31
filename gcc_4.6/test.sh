sudo docker run -t -d --name conangcc46 lasote/conangcc46 && \
sudo docker exec conangcc46 sudo pip install -U conan_package_tools && \
sudo docker exec conangcc46 sudo pip install -U conan && \
sudo docker exec conangcc46 conan user && \
sudo docker exec conangcc46 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=gcc -s compiler.version=4.6 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conangcc46 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=gcc -s compiler.version=4.6 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conangcc46 && \
sudo docker rm conangcc46
