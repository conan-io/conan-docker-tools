FROM conanio/gcc8

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CC=aarch64-linux-gnu-gcc-8 \
    CXX=aarch64-linux-gnu-g++-8 \
    CMAKE_C_COMPILER=aarch64-linux-gnu-gcc-8 \
    CMAKE_CXX_COMPILER=aarch64-linux-gnu-g++-8 \
    STRIP=aarch64-linux-gnu-strip \
    RANLIB=aarch64-linux-gnu-ranlib \
    AS=aarch64-linux-gnu-as \
    AR=aarch64-linux-gnu-ar \
    LD=aarch64-linux-gnu-ld \
    FC=aarch64-linux-gnu-gfortran-8

COPY sources.list /etc/apt/sources.list
COPY arm64.list /etc/apt/sources.list.d/arm64.list

RUN dpkg --add-architecture arm64 \
    && apt-get -qq update \
    && apt-get install -y --no-install-recommends \
       ".*8.*aarch64-linux-gnu.*" \
    && update-alternatives --install /usr/bin/aarch64-linux-gnu-gcc aarch64-linux-gnu-gcc /usr/bin/aarch64-linux-gnu-gcc-8 100 \
    && update-alternatives --install /usr/bin/aarch64-linux-gnu-g++ aarch64-linux-gnu-g++ /usr/bin/aarch64-linux-gnu-g++-8 100 \
    && update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov aarch64-linux-gnu-gcov /usr/bin/aarch64-linux-gnu-gcov-8 100 \
    && update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov-dump aarch64-linux-gnu-gcov-dump /usr/bin/aarch64-linux-gnu-gcov-dump-8 100 \
    && update-alternatives --install /usr/bin/aarch64-linux-gnu-gcov-tool aarch64-linux-gnu-gcov-tool /usr/bin/aarch64-linux-gnu-gcov-tool-8 100 \
    && rm -rf /var/lib/apt/lists/* \
    && pip install -q --no-cache-dir conan conan-package-tools --upgrade \
    && profile new default --detect \
    && profile update settings.arch=armv8 default
