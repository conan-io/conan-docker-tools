FROM lasote/conangcc6

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=arm-linux-gnueabi-gcc \
    CXX=arm-linux-gnueabi-g++ \
    CMAKE_C_COMPILER=arm-linux-gnueabi-gcc \
    CMAKE_CXX_COMPILER=arm-linux-gnueabi-g++ \
    STRIP=arm-linux-gnueabi-strip \
    RANLIB=arm-linux-gnueabi-ranlib\
    AS=arm-linux-gnueabi-as \
    AR=arm-linux-gnueabi-ar \
    LD=arm-linux-gnueabi-ld

RUN sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends \
       gcc-arm-linux-gnueabi \
       g++-arm-linux-gnueabi \
       binutils-arm-linux-gnueabi \
    && sudo rm -rf /var/lib/apt/lists/* \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7 default
