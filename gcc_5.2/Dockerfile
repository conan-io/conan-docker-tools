FROM ubuntu:wily

MAINTAINER Luis Martinez de Bartolome

RUN dpkg --add-architecture i386 && rm -rf /var/lib/apt/lists/* && apt-get update && apt-get install -y python-dev sudo build-essential wget git vim libc6-dev-i386 g++-multilib nasm dh-autoreconf valgrind ninja-build  libffi-dev libssl-dev
# RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
# Install CMake 3
RUN wget https://cmake.org/files/v3.9/cmake-3.9.0-Linux-x86_64.tar.gz --no-check-certificate && tar -xzf cmake-3.9.0-Linux-x86_64.tar.gz && cp -fR cmake-3.9.0-Linux-x86_64/* /usr && rm -rf cmake-3.9.0-Linux-x86_64 && rm cmake-3.9.0-Linux-x86_64.tar.gz
RUN wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate && python get-pip.py && pip install -U pip
RUN pip install conan
RUN groupadd 1001 -g 1001
RUN groupadd 1000 -g 1000
RUN groupadd 2000 -g 2000
RUN groupadd 999 -g 999
RUN useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 && echo "conan:conan" | chpasswd && adduser conan sudo
RUN echo "conan ALL= NOPASSWD: ALL\n" >> /etc/sudoers
USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
