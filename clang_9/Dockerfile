FROM ubuntu:eoan AS basics

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV LLVM_VERSION=9.0 \
    CMAKE_VERSION_MAJOR_MINOR=3.18 \
    CMAKE_VERSION_FULL=3.18.2 \
    CC=clang \
    CXX=clang++ \
    CMAKE_C_COMPILER=clang \
    CMAKE_CXX_COMPILER=clang++ \
    PYENV_ROOT=/opt/pyenv \
    PATH=/opt/pyenv/shims:${PATH}

COPY sources.list /etc/apt/sources.list

RUN dpkg --add-architecture i386 \
    && apt-get -qq update \
    && apt-get install -y --no-install-recommends \
       sudo=1.* \
       wget=1.* \
       git=1:2.* \
       g++-multilib=4:9.* \
       clang-9=1:9* \
       make=4.* \
       libc6-dev-i386=2.* \
       libgmp-dev=2:6.* \
       libmpfr-dev=4.* \
       libmpc-dev=1.* \
       nasm=2.* \
       dh-autoreconf=19 \
       libffi-dev=3.* \
       libssl-dev=1* \
       ninja-build=1.* \
       libc++-dev=1:9.* \
       libc++abi-dev=1:9.* \
       pkg-config=0.* \
       subversion=1.* \
       zlib1g-dev=1:1.* \
       libbz2-dev=1.* \
       libsqlite3-dev=3.* \
       libreadline-dev=8.* \
       xz-utils=5.* \
       curl=7.* \
       libncurses5-dev=6.* \
       libncursesw5-dev=6.* \
       liblzma-dev=5.* \
       gnupg=2.* \
       ca-certificates \
       # libc++abi-dev:i386=1:9.* \
       # libc++-dev:i386=1:9.* \
    && update-alternatives --install /usr/bin/clang++ clang++ /usr/bin/clang++-9 100 \
    && update-alternatives --install /usr/bin/clang clang /usr/bin/clang-9 100 \
    && update-alternatives --install /usr/bin/cc cc /usr/bin/clang-9 100 \
    && update-alternatives --install /usr/bin/c++ c++ /usr/bin/clang++-9 100 \
    && update-alternatives --install /usr/bin/cpp cpp /usr/bin/clang++-9 100 \
    && ln -s /usr/include/locale.h /usr/include/xlocale.h \
    && rm -rf /var/lib/apt/lists/* \
    && wget -q --no-check-certificate -O /usr/local/bin/jfrog https://api.bintray.com/content/jfrog/jfrog-cli-go/\$latest/jfrog-cli-linux-amd64/jfrog?bt_package=jfrog-cli-linux-amd64 \
    && chmod +x /usr/local/bin/jfrog \
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
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.7.5 \
    && pyenv global 3.7.5 \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools \
    && chown -R conan:1001 /opt/pyenv \
    # remove all __pycache__ directories created by pyenv
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf \
    && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100


FROM basics AS building_layer 

RUN mkdir conan_packages \
    && cd conan_packages \
    # Temporary dependencies for (potential) boostrapping purposes 
    && wget --no-check-certificate --quiet https://cmake.org/files/v${CMAKE_VERSION_MAJOR_MINOR}/cmake-${CMAKE_VERSION_FULL}.tar.gz \
    && tar -xzf cmake-${CMAKE_VERSION_FULL}.tar.gz \
    && cd cmake-${CMAKE_VERSION_FULL} \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && cd - \
    && rm -rf cmake-* \
    # Install Packages which we want to deploy
    # Install CMake + move license files to specific licenses/cmake subdirectory for deploy
    && conan install cmake/${CMAKE_VERSION_FULL}@ --build missing -g deploy \
    && cd cmake/licenses \
    && mkdir cmake \ 
    && ls | grep -v cmake | xargs mv -t cmake


FROM basics AS final_image 

USER conan
WORKDIR /home/conan

COPY --from=building_layer /conan_packages/cmake/ /usr/

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
