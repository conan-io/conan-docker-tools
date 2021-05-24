FROM conanio/gcc6

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV CC=arm-linux-gnueabi-gcc \
    CXX=arm-linux-gnueabi-g++ \
    CMAKE_C_COMPILER=arm-linux-gnueabi-gcc \
    CMAKE_CXX_COMPILER=arm-linux-gnueabi-g++ \
    STRIP=arm-linux-gnueabi-strip \
    RANLIB=arm-linux-gnueabi-ranlib\
    AS=arm-linux-gnueabi-as \
    AR=arm-linux-gnueabi-ar \
    LD=arm-linux-gnueabi-ld \
    FC=arm-linux-gnueabi-gfortran-6

RUN sudo apt-get -qq update \
    && sudo apt-get -qq install -y --force-yes --no-install-recommends --no-install-suggests \
       ".*6.*arm-linux-gnueabi.*" \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-g++ arm-linux-gnueabi-g++ /usr/bin/arm-linux-gnueabi-g++-6 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-c++ arm-linux-gnueabi-c++ /usr/bin/arm-linux-gnueabi-g++-6 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-gcc arm-linux-gnueabi-gcc /usr/bin/arm-linux-gnueabi-gcc-6 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabi-cc arm-linux-gnueabi-cc /usr/bin/arm-linux-gnueabi-gcc-6 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7 default
