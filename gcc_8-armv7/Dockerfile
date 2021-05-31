FROM conanio/gcc8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV CC=arm-linux-gnueabi-gcc-8 \
    CXX=arm-linux-gnueabi-g++-8 \
    CMAKE_C_COMPILER=arm-linux-gnueabi-gcc-8 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabi-g++-8 \
    STRIP=arm-linux-gnueabi-strip \
    RANLIB=arm-linux-gnueabi-ranlib \
    AS=arm-linux-gnueabi-as \
    AR=arm-linux-gnueabi-ar \
    LD=arm-linux-gnueabi-ld \
    FC=arm-linux-gnueabi-gfortran-8

RUN sudo apt-get -qq update \
    && sudo apt-get install -y --no-install-recommends --no-install-suggests \
       ".*8.*arm-linux-gnueabi.*" \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcc arm-linux-gnueabi-gcc /usr/bin/arm-linux-gnueabi-gcc-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-g++ arm-linux-gnueabi-g++ /usr/bin/arm-linux-gnueabi-g++-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcov arm-linux-gnueabi-gcov /usr/bin/arm-linux-gnueabi-gcov-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcov-dump arm-linux-gnueabi-gcov-dump /usr/bin/arm-linux-gnueabi-gcov-dump-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcov-tool arm-linux-gnueabi-gcov-tool /usr/bin/arm-linux-gnueabi-gcov-tool-8 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7 default
