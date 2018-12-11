FROM i386/centos:6

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV PATH=/opt/rh/devtoolset-7/root/usr/bin:${PATH:+:${PATH}} \
    MANPATH=/opt/rh/devtoolset-7/root/usr/share/man${MANPATH:+:${MANPATH}} \
    INFOPATH=/opt/rh/devtoolset-7/root/usr/share/info${INFOPATH:+:${INFOPATH}} \
    PCP_DIR=/opt/rh/devtoolset-7/root \
    PERL5LIB=/opt/rh/devtoolset-7/root//usr/lib64/perl5/vendor_perl:/opt/rh/devtoolset-7/root/usr/lib/perl5:/opt/rh/devtoolset-7/root//usr/share/perl5/vendor_perl${PERL5LIB:+:${PERL5LIB}} \
    LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib64:/opt/rh/devtoolset-7/root/usr/lib:/opt/rh/devtoolset-7/root/usr/lib64/dyninst:/opt/rh/devtoolset-7/root/usr/lib/dyninst${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

COPY cloudlinux.repo /etc/yum.repos.d/cloudlinux.repo

RUN printf "i686" >  /etc/yum/vars/arch \
    && printf "i386" >  /etc/yum/vars/basearch \
    && yum update -y \
    && yum install -y \
       sudo \
       wget \
       git \
       make \
       valgrind \
       glibc-devel \
       gmp-devel \
       mpfr-devel \
       libmpc-devel \
       nasm \
       autoconf \
       libffi-devel \
       openssl-devel \
       pkgconfig \
       subversion \
       zlib-devel \
       xz \
       curl \
       xz-devel \
       tar \
       devtoolset-7-toolchain \
    && yum clean all \
    && wget --no-check-certificate --quiet -O /tmp/cmake-3.12.1.tar.gz https://cmake.org/files/v3.12/cmake-3.12.1.tar.gz \
    && tar -xzf /tmp/cmake-3.12.1.tar.gz -C /tmp \
    && pushd /tmp/cmake-3.12.1 \
    && ./bootstrap > /dev/null \
    && make -s -j`nproc` \
    && make -s install > /dev/null \
    && popd \
    && rm -rf /tmp/cmake-

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir conan \
    && sed -i 's/# %wheel/%wheel/g' /etc/sudoers

RUN groupadd 1001 -g 1001 \
    && useradd -ms /bin/bash conan -g 1001 -G wheel \
    && printf "conan:conan" | chpasswd

USER conan
WORKDIR /home/conan



