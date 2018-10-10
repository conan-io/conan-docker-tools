FROM conanio/conangcc52

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=arm-linux-gnueabi-gcc-4.9 \
    CXX=arm-linux-gnueabi-g++-4.9 \
    CMAKE_C_COMPILER=arm-linux-gnueabi-gcc-4.9 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabi-g++-4.9 \
    STRIP=arm-linux-gnueabi-strip \
    RANLIB=arm-linux-gnueabi-gcc-ranlib-4.9\
    AS=arm-linux-gnueabi-as \
    AR=arm-linux-gnueabi-gcc-ar-4.9 \
    LD=arm-linux-gnueabi-ld \
    FC=arm-linux-gnueabi-gfortran-4.9

RUN sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends \
       ".*4\.9.*arm-linux-gnueabi.*" \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo pip install -q --no-cache-dir conan --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7 default
