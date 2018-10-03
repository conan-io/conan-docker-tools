docker run -t -d --name conanmsvc14 lasote/conanmsvc14 && \
docker exec conanmsvc14 pip install -U conan_package_tools && \
docker exec conanmsvc14 pip install -U conan && \
docker exec conanmsvc14 conan user && \
docker exec conanmsvc14 conan install gtest/1.8.0@lasote/stable -s arch=x86_64 -s compiler="Visual Studio" -s compiler.version=14 -s compiler.runtime=MD --build && \
docker exec conanmsvc14 conan install gtest/1.8.0@lasote/stable -s arch=x86 -s compiler="Visual Studio" -s compiler.version=14 -s compiler.runtime=MD --build && \
docker stop conanmsvc14 && \
docker rm conanmsvc14
