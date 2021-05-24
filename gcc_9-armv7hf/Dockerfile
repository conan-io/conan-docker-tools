FROM conanio/gcc9

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV CC=arm-linux-gnueabihf-gcc-9 \
    CXX=arm-linux-gnueabihf-g++-9 \
    CMAKE_C_COMPILER=arm-linux-gnueabihf-gcc-9 \
    CMAKE_CXX_COMPILER=arm-linux-gnueabihf-g++-9 \
    STRIP=arm-linux-gnueabihf-strip \
    RANLIB=arm-linux-gnueabihf-ranlib \
    AS=arm-linux-gnueabihf-as \
    AR=arm-linux-gnueabihf-ar \
    LD=arm-linux-gnueabihf-ld \
    FC=arm-linux-gnueabihf-gfortran-9

COPY armhf.list /etc/apt/sources.list.d/armhf.list

RUN sudo dpkg --add-architecture armhf \
    && sudo sed -i 's/deb\s/deb \[arch=amd64,i386\] /' /etc/apt/sources.list \
    && sudo apt -qq update \
    && sudo apt install -y --no-install-recommends --no-install-suggests ".*9.*arm-linux-gnueabihf.*" \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcc arm-linux-gnueabihf-gcc /usr/bin/arm-linux-gnueabihf-gcc-9 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-g++ arm-linux-gnueabihf-g++ /usr/bin/arm-linux-gnueabihf-g++-9 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov arm-linux-gnueabihf-gcov /usr/bin/arm-linux-gnueabihf-gcov-9 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-dump arm-linux-gnueabihf-gcov-dump /usr/bin/arm-linux-gnueabihf-gcov-dump-9 100 \
    && sudo update-alternatives --install /usr/bin/arm-linux-gnueabihf-gcov-tool arm-linux-gnueabihf-gcov-tool /usr/bin/arm-linux-gnueabihf-gcov-tool-9 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv7hf default
