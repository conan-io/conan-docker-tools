FROM i386/ubuntu:cosmic
ENTRYPOINT ["linux32", "--"]  # https://github.com/conan-io/conan-docker-tools/issues/36

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV LLVM_VERSION=7.0 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++ \
    CONAN_ENV_ARCH=x86

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python3-dev=3.6.6-1 \
       sudo=1.8.23-2ubuntu1 \
       wget=1.19.5-1ubuntu1 \
       git=1:2.17.1-1ubuntu1 \
       vim=2:8.0.1766-1ubuntu1 \
       g++-multilib=4:8.2.0-1ubuntu1 \
       clang-7=1:7-3 \
       make=4.2.1-1.2 \
       valgrind=1:3.13.0-2ubuntu6 \
       libc6-dev=2.28-0ubuntu1 \
       libgmp-dev=2:6.1.2+dfsg-3 \
       libmpfr-dev=4.0.1-1 \
       libmpc-dev=1.1.0-1 \
       nasm=2.13.03-2 \
       dh-autoreconf=19 \
       libffi-dev=3.2.1-8 \
       libssl-dev=1.1.1-1ubuntu2 \
       ninja-build=1.8.2-1 \
       libc++-dev=6.0.1-1 \
       libc++abi-dev=6.0.1-1 \
       pkg-config=0.29.1-0ubuntu2 \
       subversion=1.10.0-2ubuntu2 \
       ca-certificates=20180409 \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-7 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-7 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-7 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-7 100 \
    && update-alternatives --install /usr/bin/cpp cpp /usr/bin/clang++-7 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.12/cmake-3.12.1.tar.gz \
    && tar -xzf cmake-3.12.1.tar.gz \
    && cd cmake-3.12.1 \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
    && wget -q --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
    && python3 get-pip.py \
    && rm get-pip.py \
    && pip install -q -U pip \
    && pip install -q --no-cache-dir virtualenv --upgrade \
    && pip install -q --no-cache-dir conan --upgrade \
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
