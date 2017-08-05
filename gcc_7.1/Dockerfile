FROM ubuntu:artful

MAINTAINER Luis Martinez de Bartolome

RUN dpkg --add-architecture i386 \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get -qq update \
    # Install gcc and dependencies
    && apt-get -qq install -y python-dev sudo binutils wget git vim libc6-dev-i386 g++-7-multilib libgmp-dev libmpfr-dev libmpc-dev libc6-dev nasm dh-autoreconf valgrind ninja-build libffi-dev libssl-dev \
    # Update gcc order
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 10  \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 20 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 10  \
    && update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-6 20 \
    && update-alternatives --install /usr/bin/cpp cpp-bin /usr/bin/cpp-7 10  \
    && update-alternatives --set g++ /usr/bin/g++-7 \
    && update-alternatives --set gcc /usr/bin/gcc-7 \
    && update-alternatives --set cpp-bin /usr/bin/cpp-7 \
    # Install CMake
    && wget https://cmake.org/files/v3.8/cmake-3.8.1-Linux-x86_64.tar.gz --no-check-certificate -q \
    && tar -xzf cmake-3.8.1-Linux-x86_64.tar.gz \
    && cp -fR cmake-3.8.1-Linux-x86_64/* /usr \
    && rm -rf cmake-3.8.1-Linux-x86_64 \
    && rm cmake-3.8.1-Linux-x86_64.tar.gz \
    # Install Python pip
    && wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate \
    && python get-pip.py \
    && pip install -q -U pip \
    # Install Conan
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
