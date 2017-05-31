sudo docker run -t -d --name conanclang40 lasote/conanclang40 && \
sudo docker exec conanclang40 sudo pip install -U conan_package_tools && \
sudo docker exec conanclang40 sudo pip install -U conan && \
sudo docker exec conanclang40 conan user && \
sudo docker exec conanclang40 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler=clang -s compiler.version=4.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker exec conanclang40 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler=clang -s compiler.version=4.0 -s compiler.libcxx=libstdc++ --build && \
sudo docker stop conanclang40 && \
sudo docker rm conanclang40
