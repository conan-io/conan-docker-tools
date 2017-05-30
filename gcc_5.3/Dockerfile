FROM ubuntu:xenial

MAINTAINER Luis Martinez de Bartolome

RUN dpkg --add-architecture i386 && rm -rf /var/lib/apt/lists/* && apt-get update && apt-get install -y python-dev sudo build-essential wget git vim libc6-dev-i386 g++-multilib libgmp-dev libmpfr-dev libmpc-dev libc6-dev nasm dh-autoreconf valgrind && apt-get install -y --allow-downgrades gcc-5=5.3.1-14ubuntu2 gcc-5-base=5.3.1-14ubuntu2 cpp-5=5.3.1-14ubuntu2 libcc1-0=5.3.1-14ubuntu2 libgcc-5-dev=5.3.1-14ubuntu2 libstdc++6=5.3.1-14ubuntu2 libgomp1=5.3.1-14ubuntu2 libitm1=5.3.1-14ubuntu2 libatomic1=5.3.1-14ubuntu2 libasan2=5.3.1-14ubuntu2 liblsan0=5.3.1-14ubuntu2 libtsan0=5.3.1-14ubuntu2 libubsan0=5.3.1-14ubuntu2 libcilkrts5=5.3.1-14ubuntu2 libmpx0=5.3.1-14ubuntu2 libquadmath0=5.3.1-14ubuntu2 gcc-5-multilib=5.3.1-14ubuntu2 lib32gcc-5-dev=5.3.1-14ubuntu2 libx32gcc-5-dev=5.3.1-14ubuntu2 lib32gomp1=5.3.1-14ubuntu2 libx32gomp1=5.3.1-14ubuntu2 lib32itm1=5.3.1-14ubuntu2 libx32itm1=5.3.1-14ubuntu2 lib32atomic1=5.3.1-14ubuntu2 libx32atomic1=5.3.1-14ubuntu2 lib32asan2=5.3.1-14ubuntu2 libx32asan2=5.3.1-14ubuntu2 lib32ubsan0=5.3.1-14ubuntu2 libx32ubsan0=5.3.1-14ubuntu2 lib32cilkrts5=5.3.1-14ubuntu2 libx32cilkrts5=5.3.1-14ubuntu2 lib32mpx0=5.3.1-14ubuntu2 lib32quadmath0=5.3.1-14ubuntu2 libx32quadmath0=5.3.1-14ubuntu2 lib32stdc++6=5.3.1-14ubuntu2 libx32stdc++6=5.3.1-14ubuntu2 linux-libc-dev:i386 libstdc++-5-dev=5.3.1-14ubuntu2 && apt-get install -y --allow-downgrades g++-5=5.3.1-14ubuntu2 libstdc++-5-dev=5.3.1-14ubuntu2 g++-5-multilib=5.3.1-14ubuntu2 lib32stdc++-5-dev=5.3.1-14ubuntu2 libx32stdc++-5-dev=5.3.1-14ubuntu2 ninja-build
RUN ln -s /usr/bin/g++-5 /usr/bin/g++
# RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Install CMake 3
RUN wget https://cmake.org/files/v3.8/cmake-3.8.1-Linux-x86_64.tar.gz --no-check-certificate && tar -xzf cmake-3.8.1-Linux-x86_64.tar.gz && cp -fR cmake-3.8.1-Linux-x86_64/* /usr && rm -rf cmake-3.8.1-Linux-x86_64 && rm cmake-3.8.1-Linux-x86_64.tar.gz

RUN wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate && python get-pip.py && pip install -U pip
RUN pip install conan
RUN groupadd 1001 -g 1001
RUN groupadd 1000 -g 1000
RUN useradd -ms /bin/bash conan -g 1001 -G 1000 && echo "conan:conan" | chpasswd && adduser conan sudo
RUN echo "conan ALL= NOPASSWD: ALL\n" >> /etc/sudoers
USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
