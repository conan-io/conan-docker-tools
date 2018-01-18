FROM ubuntu:zesty

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV LLVM_VERSION=3.9 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       python-dev=2.7.* \
       sudo=1.8.* \
       wget=1.18* \
       git=1:2.* \
       vim=2:8.* \
       clang-${LLVM_VERSION}=1:3.9.1-* \
       llvm-${LLVM_VERSION}=1:3.9.1-* \
       llvm-${LLVM_VERSION}-dev=1:3.9.1-* \
       llvm-${LLVM_VERSION}-runtime=1:3.9.1-* \
       llvm=1:4.0-* \
       make=4.1-* \
       valgrind=1:3.* \
       libc6-dev-i386=2.24-* \
       g++-multilib=4:6.3.* \
       libgmp-dev=2:6.1.* \
       libmpfr-dev=3.1.* \
       libmpc-dev=1.0.* \
       nasm=2.12.* \
       dh-autoreconf=13 \
       libffi-dev=3.2.* \
       libssl-dev=1.0.* \
       ninja-build=1.7.* \
       libc++-dev=3.9.* \
       libc++-dev:i386=3.9.* \
       libc++abi-dev=3.9.* \
       libc++abi-dev:i386=3.9.* \
       ca-certificates \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q --no-check-certificate https://cmake.org/files/v3.10/cmake-3.10.1-Linux-x86_64.tar.gz \
    && tar -xzf cmake-3.10.1-Linux-x86_64.tar.gz \
    && cp -fR cmake-3.10.1-Linux-x86_64/* /usr \
    && rm -rf cmake-3.10.1-Linux-x86_64 \
    && rm cmake-3.10.1-Linux-x86_64.tar.gz \
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
