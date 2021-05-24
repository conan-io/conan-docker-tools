FROM conanio/gcc5

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV CC=arm-linux-gnueabihf-gcc-5 \
    CXX=arm-linux-gnueabihf-g++-5 \
    CMAKE_C_COMPILER=arm-linux-gnueabihf-gcc-5 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++-5 \
    STRIP=arm-linux-gnueabihf-strip \
    RANLIB=arm-linux-gnueabihf-ranlib\
    AS=arm-linux-gnueabihf-as \
    AR=arm-linux-gnueabihf-ar \
    LD=arm-linux-gnueabihf-ld \
    FC=arm-linux-gnueabihf-gfortran-5

COPY sources.list /etc/apt/sources.list
COPY armhf.list /etc/apt/sources.list.d/armhf.list

RUN sudo dpkg --add-architecture armhf \
    && sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends --no-install-suggests \
       ".*5.*arm-linux-gnueabihf.*" \
       binutils-arm-linux-gnueabi \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-g++ arm-linux-gnueabihf-g++ /usr/bin/arm-linux-gnueabihf-g++-5 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-c++ arm-linux-gnueabihf-c++ /usr/bin/arm-linux-gnueabihf-g++-5 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcc arm-linux-gnueabihf-gcc /usr/bin/arm-linux-gnueabihf-gcc-5 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-cc arm-linux-gnueabihf-cc /usr/bin/arm-linux-gnueabihf-gcc-5 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
