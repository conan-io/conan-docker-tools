FROM ubuntu:trusty

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends \
       sudo=1.8.* \
       build-essential=11.* \
       wget=1.15-* \
       git=1:1.9.* \
       vim=2:7.4.* \
       libc6-dev-i386=2.19-* \
       g++-multilib=4:4.8.* \
       nasm=2.10.* \
       dh-autoreconf=9 \
       valgrind=1:3.10.* \
       ninja-build=1.3.* \
       libffi-dev=3.1* \
       libssl-dev=1.0.* \
       pkg-config=0.26-1ubuntu4 \
       subversion=1.8.8-1ubuntu3.3 \
       zlib1g-dev=1:1.* \
       libbz2-dev=1.* \
       libsqlite3-dev=3.* \
       libreadline-dev=6.* \
       xz-utils=5.* \
       curl=7.* \
       libncurses5-dev=5.* \
       libncursesw5-dev=5.* \
       liblzma-dev=5.* \
       ca-certificates \
    && update-ca-certificates \
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
    && sed -i '0,/python3/s//python/' /usr/bin/lsb_release \
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.6.7 \
    && pyenv global 3.6.7 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools \
    && chown -R conan:1001 /opt/pyenv \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100 \
    && update-alternatives --install /usr/local/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/local/bin/pip pip /opt/pyenv/shims/pip 100

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
