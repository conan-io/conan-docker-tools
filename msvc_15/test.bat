docker run -t -d --name conanmsvc15 lasote/conanmsvc15 && \
docker exec conanmsvc15 pip install -U conan_package_tools && \
docker exec conanmsvc15 pip install -U conan && \
docker exec conanmsvc15 conan user && \
docker exec conanmsvc15 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler="Visual Studio" -s compiler.version=15 -s compiler.runtime=MD --build && \
docker exec conanmsvc15 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler="Visual Studio" -s compiler.version=15 -s compiler.runtime=MD --build && \
docker stop conanmsvc15 && \
docker rm conanmsvc15
