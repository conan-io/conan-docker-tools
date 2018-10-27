docker run -t -d --name msvc14 conanio/msvc14 && \
docker exec msvc14 pip install -U conan_package_tools && \
docker exec msvc14 pip install -U conan && \
docker exec msvc14 conan user && \
docker exec msvc14 conan install gtest/1.8.1@bincrafters/stable -s arch=x86_64 -s compiler="Visual Studio" -s compiler.version=14 -s compiler.runtime=MD --build && \
docker exec msvc14 conan install gtest/1.8.1@bincrafters/stable -s arch=x86 -s compiler="Visual Studio" -s compiler.version=14 -s compiler.runtime=MD --build && \
docker stop msvc14 && \
docker rm msvc14
