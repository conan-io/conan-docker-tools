FROM conanio/conangcc8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=arm-linux-gnueabihf-gcc-8 \
    CXX=arm-linux-gnueabihf-g++-8 \
    CMAKE_C_COMPILER=arm-linux-gnueabihf-gcc-8 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++-8 \
    STRIP=arm-linux-gnueabihf-strip \
    RANLIB=arm-linux-gnueabihf-ranlib \
    AS=arm-linux-gnueabihf-as \
    AR=arm-linux-gnueabihf-ar \
    LD=arm-linux-gnueabihf-ld \
    FC=arm-linux-gnueabihf-gfortran-8

RUN sudo apt-get -qq update \
    && sudo apt-get install -y --no-install-recommends \
       ".*8.*arm-linux-gnueabihf.*" \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo pip install -q --no-cache-dir conan --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
