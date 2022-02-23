FROM conanio/gcc9

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION

ENV CC=aarch64-linux-gnu-gcc-9 \
    CXX=aarch64-linux-gnu-g++-9 \
    CMAKE_C_COMPILER=aarch64-linux-gnu-gcc-9 \
    CMAKE_CXX_COMPILER=aarch64-linux-gnu-g++-9 \
    STRIP=aarch64-linux-gnu-strip \
    RANLIB=aarch64-linux-gnu-ranlib \
    AS=aarch64-linux-gnu-as \
    AR=aarch64-linux-gnu-ar \
    LD=aarch64-linux-gnu-ld \
    FC=aarch64-linux-gnu-gfortran-9

COPY arm64.list /etc/apt/sources.list.d/arm64.list

RUN sudo dpkg --add-architecture arm64 \
    && sudo sed -i 's/deb\s/deb \[arch=amd64,i386\] /' /etc/apt/sources.list \
    && sudo apt-get -qq update \
    && sudo apt-get install -y --no-install-recommends --no-install-suggests \
       ".*9.*aarch64-linux-gnu.*" \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcc aarch64-linux-gnu-gcc /usr/bin/aarch64-linux-gnu-gcc-9 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-g++ aarch64-linux-gnu-g++ /usr/bin/aarch64-linux-gnu-g++-9 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov aarch64-linux-gnu-gcov /usr/bin/aarch64-linux-gnu-gcov-9 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov-dump aarch64-linux-gnu-gcov-dump /usr/bin/aarch64-linux-gnu-gcov-dump-9 100 \
    && sudo update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov-tool aarch64-linux-gnu-gcov-tool /usr/bin/aarch64-linux-gnu-gcov-tool-9 100 \
    && sudo rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan==${CONAN_VERSION} conan-package-tools --upgrade \
    && conan profile new default --detect \
    && conan profile update settings.arch=armv8 default
