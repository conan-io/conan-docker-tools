FROM lasote/conangcc5

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

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

RUN sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends \
       ".*5.*arm-linux-gnueabihf.*" \
       binutils-arm-linux-gnueabi \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo pip install -q --no-cache-dir conan --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
