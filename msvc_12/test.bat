docker run -t -d --name conanmsvc12 lasote/conanmsvc12 && \
docker exec conanmsvc12 pip install -U conan_package_tools && \
docker exec conanmsvc12 pip install -U conan && \
docker exec conanmsvc12 conan user && \
docker exec conanmsvc12 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler="Visual Studio" -s compiler.version=12 -s compiler.runtime=MD --build && \
docker exec conanmsvc12 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler="Visual Studio" -s compiler.version=12 -s compiler.runtime=MD --build && \
docker stop conanmsvc12 && \
docker rm conanmsvc12
