FROM ubuntu:wily

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

RUN sed -i -re 's/([a-z]{2}\.)?archive.ubuntu.com|security.ubuntu.com/old-releases.ubuntu.com/g' /etc/apt/sources.list \
    && dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
    sudo=1.8.* \
    build-essential=12.* \
    wget=1.16.* \
    git=1:2.5.* \
    vim=2:7.4.* \
    libc6-dev-i386=2.21-* \
    g++-multilib=4:5.2.* \
    nasm=2.11.* \
    dh-autoreconf=10 \
    valgrind=1:3.11.* \
    ninja-build=1.3.* \
    libffi-dev=3.2.* \
    libssl-dev=1.0.2* \
    pkg-config=0.28-1ubuntu1 \
    subversion=1.8.13-1ubuntu3 \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
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
