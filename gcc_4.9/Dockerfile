FROM ubuntu:trusty

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && add-apt-repository -y ppa:ubuntu-toolchain-r/test \
    && apt-get -qq update \
    && apt-get install -y --force-yes --no-install-recommends \
       sudo=1.8.9p5-1ubuntu1.4 \
       g++-4.9=4.9.4-2ubuntu1~14.04.1 \
       g++-4.9-multilib=4.9.4-2ubuntu1~14.04.1 \
       libc6-dev-i386=2.19-0ubuntu6.14 \
       gcc-multilib=4:4.8.2-1ubuntu6 \
       wget=1.15-1ubuntu1.14.04.4 \
       git \
       vim=2:7.4.052-1ubuntu3.1 \
       nasm=2.10.09-1 \
       dh-autoreconf=9 \
       valgrind=1:3.10.1-1ubuntu3~14.5 \
       ninja-build=1.3.4-1.1ubuntu0.14.04.1 \
       libffi-dev=3.1~rc1+r3.0.13-12ubuntu0.2 \
       libssl-dev=1.* \
       pkg-config=0.26-1ubuntu4 \
       subversion=1.8.8-1ubuntu3.3 \
       ca-certificates=20170717~14.04.1 \
    && rm -rf /var/lib/apt/lists/* \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.9 100 \
    && wget -q --no-check-certificate https://cmake.org/files/v3.12/cmake-3.12.1-Linux-x86_64.tar.gz \
    && tar -xzf cmake-3.12.1-Linux-x86_64.tar.gz \
    && cp -fR cmake-3.12.1-Linux-x86_64/* /usr \
    && rm -rf cmake-3.12.1-Linux-x86_64 \
    && rm cmake-3.12.1-Linux-x86_64.tar.gz \
    && groupadd 1001 -g 1001 \
    && groupadd 1000 -g 1000 \
    && groupadd 2000 -g 2000 \
    && groupadd 999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers \
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && pyenv install 3.7.0 \
    && pyenv global 3.7.0 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan \
    && chown -R conan:1001 /opt/pyenv

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
