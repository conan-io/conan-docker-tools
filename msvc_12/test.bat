docker run -t -d --name msvc12 conanio/msvc12 && \
docker exec msvc12 pip install -U conan_package_tools && \
docker exec msvc12 pip install -U conan && \
docker exec msvc12 conan user && \
docker exec msvc12 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler="Visual Studio" -s compiler.version=12 -s compiler.runtime=MD --build && \
docker exec msvc12 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler="Visual Studio" -s compiler.version=12 -s compiler.runtime=MD --build && \
docker stop msvc12 && \
docker rm msvc12
