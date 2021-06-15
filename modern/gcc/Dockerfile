ARG DOCKER_USERNAME

FROM ubuntu:xenial as gcc-builder

ARG GCC_VERSION ARTIFACTORY_REPOSITORY LIBSTDCPP_VERSION

LABEL maintainer="Conan.io <info@conan.io>"

RUN apt-get -qq update \
    && apt-get -qq install -y --no-install-recommends --no-install-suggests -o=Dpkg::Use-Pty=0 \
       g++-multilib \
       gcc \
       curl \
       wget \
       zlib1g \
       ca-certificates \
       autoconf-archive \
       binutils \
       libgmp-dev \
       libmpfr-dev \
       libmpc-dev \
       nasm \
       dh-autoreconf \
       libffi-dev \
       libssl-dev \
       pkg-config \
    && wget -q --no-check-certificate http://mirrors.concertpass.com/gcc/releases/gcc-${GCC_VERSION}/gcc-${GCC_VERSION}.tar.xz \
    && tar Jxf gcc-${GCC_VERSION}.tar.xz \
    && cd gcc-${GCC_VERSION} \
    && ./configure --build=x86_64-linux-gnu \
                   --disable-bootstrap \
                   --disable-multilib \
                   --disable-nsl \
                   --enable-languages=c,c++,fortran \
                   --disable-werror \
                   --without-isl \
                   --with-system-zlib \
                   --prefix=/tmp/install \
    && make -s -j$(nproc) \
    && make install-strip \
    && mkdir /tmp/gcc \
    && curl -s -O "${ARTIFACTORY_REPOSITORY}/gcc-${LIBSTDCPP_VERSION}.tar.gz" \
    && tar zxf gcc-${LIBSTDCPP_VERSION}.tar.gz -C /tmp/gcc

FROM ${DOCKER_USERNAME}/base-ubuntu16.04:latest as deploy

ARG GCC_VERSION LIBSTDCPP_PATCH_VERSION

COPY --from=gcc-builder /tmp/install /tmp/install
COPY --from=gcc-builder /tmp/gcc /tmp/gcc

RUN sudo rm -rf /usr/lib/gcc/x86_64-linux-gnu/* \
    && sudo cp -a /tmp/install/lib/gcc/x86_64-linux-gnu/${GCC_VERSION} /usr/lib/gcc/x86_64-linux-gnu/ \
    && sudo cp -a /tmp/install/include/* /usr/local/include/ \
    && sudo cp -a /tmp/install/lib64/ /usr/local/ \
    && sudo cp -a /tmp/install/libexec/ /usr/local/ \
    && sudo cp -a /tmp/install/lib/* /usr/local/lib/ \
    && sudo cp -a /tmp/install/bin/* /usr/local/bin/ \
    && sudo rm -rf /tmp/install \
    && sudo mv /tmp/gcc/lib64/libstdc++.so.6.0.${LIBSTDCPP_PATCH_VERSION} /usr/local/lib64/libstdc++.so.6.0.${LIBSTDCPP_PATCH_VERSION} \
    && sudo ln -s -f /usr/local/lib64/libstdc++.so.6.0.${LIBSTDCPP_PATCH_VERSION} /usr/local/lib64/libstdc++.so.6 \
    && sudo ln -s -f /usr/local/lib64/libstdc++.so.6 /usr/local/lib64/libstdc++.so \
    && sudo rm -rf /tmp/gcc \
    && sudo update-alternatives --install /usr/local/bin/cc cc /usr/local/bin/gcc 100 \
    && sudo update-alternatives --install /usr/local/bin/cpp cpp /usr/local/bin/g++ 100 \
    && sudo update-alternatives --install /usr/local/bin/c++ c++ /usr/local/bin/g++ 100 \
    && sudo rm /etc/ld.so.cache \
    && sudo ldconfig -C /etc/ld.so.cache

FROM deploy as conan

ARG CONAN_VERSION

RUN pip install conan==${CONAN_VERSION}
