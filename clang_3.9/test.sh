sudo docker run -t -d --name conanclang39 lasote/conanclang39 && \
sudo docker exec conanclang39 sudo pip install -U conan_package_tools && \
sudo docker exec conanclang39 sudo pip install -U conan && \
sudo docker exec conanclang39 conan user && \
sudo docker exec conanclang39 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=clang -s compiler.version=3.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang39 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=clang -s compiler.version=3.9 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conanclang39 && \
sudo docker rm conanclang39
