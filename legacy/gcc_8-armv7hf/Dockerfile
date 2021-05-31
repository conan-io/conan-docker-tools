FROM conanio/gcc8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

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

COPY sources.list /etc/apt/sources.list
COPY armhf.list /etc/apt/sources.list.d/armhf.list

RUN sudo dpkg --add-architecture armhf \
    && sudo apt-get -qq update \
    && sudo apt-get install -y --no-install-recommends --no-install-suggests \
       ".*8.*arm-linux-gnueabihf.*" \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcc arm-linux-gnueabihf-gcc /usr/bin/arm-linux-gnueabihf-gcc-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-g++ arm-linux-gnueabihf-g++ /usr/bin/arm-linux-gnueabihf-g++-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov arm-linux-gnueabihf-gcov /usr/bin/arm-linux-gnueabihf-gcov-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-dump arm-linux-gnueabihf-gcov-dump /usr/bin/arm-linux-gnueabihf-gcov-dump-8 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-tool arm-linux-gnueabihf-gcov-tool /usr/bin/arm-linux-gnueabihf-gcov-tool-8 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
