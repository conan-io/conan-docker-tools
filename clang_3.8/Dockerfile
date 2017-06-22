FROM ubuntu:zesty

MAINTAINER Luis Martinez de Bartolome

ENV LLVM_VERSION=3.8 \
    CMAKE_VERSION=3.8.1 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++

RUN dpkg --add-architecture i386 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq update \
    # Install Clang and dependencies
    && apt-get -qq install -y python-dev sudo wget git vim clang-${LLVM_VERSION} llvm-${LLVM_VERSION} llvm-${LLVM_VERSION}-dev llvm-${LLVM_VERSION}-runtime llvm make valgrind libc6-dev-i386 g++-multilib libgmp-dev libmpfr-dev libmpc-dev nasm dh-autoreconf libffi-dev libssl-dev ninja-build libc++-dev libc++-dev:i386 libc++abi-dev libc++abi-dev:i386 \
    # Update Clang name
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-${LLVM_VERSION} 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-${LLVM_VERSION} 100 \
    # Install CMake
    && wget https://cmake.org/files/v3.8/cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz --no-check-certificate -q \
    && tar -xzf cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz \
    && cp -fR cmake-${CMAKE_VERSION}-Linux-x86_64/* /usr \
    && rm -rf cmake-${CMAKE_VERSION}-Linux-x86_64 \
    && rm cmake-${CMAKE_VERSION}-Linux-x86_64.tar.gz \
    # Install python pip
    && wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate -q \
    && python get-pip.py \
    && pip install -q -U pip \
    # Install conan
    && pip install -q conan \
    # Create User
    && groupadd 1001 -g 1001 \
    && groupadd 1000 -g 1000 \
    && groupadd 2000 -g 2000 \
    && groupadd 999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && echo "conan:conan" | chpasswd \
    && adduser conan sudo \
    && echo "conan ALL= NOPASSWD: ALL\n" >> /etc/sudoers

USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
