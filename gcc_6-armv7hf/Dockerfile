FROM lasote/conangcc63

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=arm-linux-gnueabihf-gcc \
    CXX=arm-linux-gnueabihf-g++ \
    CMAKE_C_COMPILER=arm-linux-gnueabihf-gcc \
    CMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++ \
    STRIP=arm-linux-gnueabihf-strip \
    RANLIB=arm-linux-gnueabihf-ranlib\
    AS=arm-linux-gnueabihf-as \
    AR=arm-linux-gnueabihf-ar \
    LD=arm-linux-gnueabihf-ld

RUN sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends \
       gcc-arm-linux-gnueabihf \
       g++-arm-linux-gnueabihf \
       binutils-arm-linux-gnueabihf \
    && sudo rm -rf /var/lib/apt/lists/* \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
