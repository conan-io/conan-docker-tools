FROM i386/ubuntu:artful
ENTRYPOINT ["linux32", "--"]  # https://github.com/conan-io/conan-docker-tools/issues/36

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV LLVM_VERSION=5.0 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++ \
    CONAN_ENV_ARCH=x86

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.14-2ubuntu1 \
       sudo=1.8.20p2-1ubuntu1 \
       wget=1.19.1-3ubuntu1 \
       git=1:2.14.1-1ubuntu4 \
       vim=2:8.0.0197-4ubuntu5 \
       g++=4:7.2.0-1ubuntu1 \
       clang-5.0=1:5.0-3 \
       make=4.1-9.1 \
       valgrind=1:3.13.0-1ubuntu2 \
       libc6-dev=2.26-0ubuntu2.1 \
       libgmp-dev=2:6.1.2+dfsg-1 \
       libmpfr-dev=3.1.6-1 \
       libmpc-dev=1.0.3-2 \
       nasm=2.13.01-2 \
       dh-autoreconf=14 \
       libffi-dev=3.2.1-6 \
       libssl-dev=1.0.2g-1ubuntu13.3 \
       ninja-build=1.7.2-3 \
       libc++-dev=3.9.1-3 \
       libc++abi-dev=3.9.1-3 \
       pkg-config \
       ca-certificates=20170717 \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-5.0 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-5.0 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-5.0 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-5.0 100 \
    && update-alternatives --install /usr/bin/cpp cpp /usr/bin/clang++-5.0 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.10/cmake-3.10.3.tar.gz \
    && tar -xzf cmake-3.10.3.tar.gz \
    && cd cmake-3.10.3 \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
    && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
    && python get-pip.py \
    && rm get-pip.py \
    && pip install -q -U pip \
    && pip install -q --no-cache-dir conan \
    && groupadd 1001 -g 1001 \
    && groupadd 1000 -g 1000 \
    && groupadd 2000 -g 2000 \
    && groupadd 999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers

USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
