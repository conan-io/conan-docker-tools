FROM conanio/gcc10

LABEL maintainer="Conan.io <info@conan.io>"

ARG CONAN_VERSION

RUN sudo dpkg --add-architecture armhf \
    && sudo sed -i 's/deb\s/deb \[arch=amd64,i386\] /' /etc/apt/sources.list \
    && sudo apt-get -qq update \
    && sudo apt-get install -y --no-install-recommends --no-install-suggests ".*10.*arm-linux-gnueabihf.*" \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcc arm-linux-gnueabihf-gcc /usr/bin/arm-linux-gnueabihf-gcc-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-g++ arm-linux-gnueabihf-g++ /usr/bin/arm-linux-gnueabihf-g++-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov arm-linux-gnueabihf-gcov /usr/bin/arm-linux-gnueabihf-gcov-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-dump arm-linux-gnueabihf-gcov-dump /usr/bin/arm-linux-gnueabihf-gcov-dump-10 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-tool arm-linux-gnueabihf-gcov-tool /usr/bin/arm-linux-gnueabihf-gcov-tool-10 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.compiler.libcxx=libstdc++11 default \
    && conan profile new armv7hf --detect \
    && conan profile update settings.arch=armv7hf armv7hf \
    && conan profile update settings.compiler.libcxx=libstdc++11 armv7hf \
    && conan profile update env.CC=/usr/bin/arm-linux-gnueabihf-gcc-10 armv7hf \
    && conan profile update env.CXX=/usr/bin/arm-linux-gnueabihf-g++-10 armv7hf \
    && conan profile update env.CMAKE_C_COMPILER=/usr/bin/arm-linux-gnueabihf-gcc-10 armv7hf \
    && conan profile update env.CMAKE_CXX_COMPILER=/usr/bin/arm-linux-gnueabihf-g++-10 armv7hf \
    && conan profile update env.STRIP=/usr/bin/arm-linux-gnueabihf-strip armv7hf \
    && conan profile update env.AS=/usr/bin/arm-linux-gnueabihf-as armv7hf \
    && conan profile update env.AR=/usr/bin/arm-linux-gnueabihf-ar armv7hf \
    && conan profile update env.LD=/usr/bin/arm-linux-gnueabihf-ld armv7hf \
    && conan profile update env.FC=/usr/bin/arm-linux-gnueabihf-gfortran-10 armv7hf \
    && conan profile update env.GCOV=/usr/bin/arm-linux-gnueabihf-gcov-10 armv7hf
