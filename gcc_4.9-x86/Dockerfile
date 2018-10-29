FROM i386/ubuntu:trusty
ENTRYPOINT ["linux32", "--"]

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV CONAN_ENV_ARCH=x86 \
    PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

RUN dpkg --add-architecture i386 \
    && printf "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty main\n" >> /etc/apt/sources.list \
    && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 60C317803A41BA51845E371A1E9377A2BA9EF27F \
    && apt-get -qq update \
    && apt-get install -y --force-yes --no-install-recommends \
       sudo=1.8.9p5-1ubuntu1.4 \
       g++-4.9=4.9.4-2ubuntu1~14.04.1 \
       g++-4.9-multilib=4.9.4-2ubuntu1~14.04.1 \
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
       zlib1g-dev=1:1.* \
       libbz2-dev=1.* \
       libsqlite3-dev=3.* \
       libreadline-dev=6.* \
       ca-certificates=20170717~14.04.1 \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.9 100 \
    && update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/gcc-4.9 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/g++-4.9 100 \
    && wget --no-check-certificate --quiet https://cmake.org/files/v3.12/cmake-3.12.1.tar.gz \
    && tar -xzf cmake-3.12.1.tar.gz \
    && cd cmake-3.12.1 \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
    && groupadd 1001 -g 1001 \
    && groupadd 1000 -g 1000 \
    && groupadd 2000 -g 2000 \
    && groupadd 999 -g 999 \
    && useradd -ms /bin/bash conan -g 1001 -G 1000,2000,999 \
    && printf "conan:conan" | chpasswd \
    && adduser conan sudo \
    && printf "conan ALL= NOPASSWD: ALL\\n" >> /etc/sudoers \
    && sed -i '0,/python3/s//python2.7/' /usr/bin/lsb_release \
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && pyenv install 3.6.7 \
    && pyenv global 3.6.7 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan \
    && chown -R conan:1001 /opt/pyenv \
    && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
