FROM centos:6

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV PATH=/opt/rh/rh-python36/root/usr/bin:/opt/rh/devtoolset-7/root/usr/bin:${PATH:+:${PATH}} \
    MANPATH=/opt/rh/rh-python36/root/usr/share/man:/opt/rh/devtoolset-7/root/usr/share/man${MANPATH:+:${MANPATH}} \
    INFOPATH=/opt/rh/devtoolset-7/root/usr/share/info${INFOPATH:+:${INFOPATH}} \
    PCP_DIR=/opt/rh/devtoolset-7/root \
    PERL5LIB=/opt/rh/devtoolset-7/root//usr/lib64/perl5/vendor_perl:/opt/rh/devtoolset-7/root/usr/lib/perl5:/opt/rh/devtoolset-7/root//usr/share/perl5/vendor_perl${PERL5LIB:+:${PERL5LIB}} \
    LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib64:/opt/rh/devtoolset-7/root/usr/lib:/opt/rh/devtoolset-7/root/usr/lib64/dyninst:/opt/rh/devtoolset-7/root/usr/lib/dyninst:/opt/rh/rh-python36/root/usr/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} \
    PKG_CONFIG_PATH=/opt/rh/rh-python36/root/usr/lib64/pkgconfig${PKG_CONFIG_PATH:+:${PKG_CONFIG_PATH}} \
    XDG_DATA_DIRS="/opt/rh/rh-python36/root/usr/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}" \
    CXX=/opt/rh/devtoolset-7/root/usr/bin/g++ \
    CC=/opt/rh/devtoolset-7/root/usr/bin/gcc

RUN yum update -y \
    && yum install -y centos-release-scl \
    && yum install -y \
       sudo \
       wget \
       git \
       make \
       glibc-devel \
       glibc-devel.i686 \
       libgcc.i686 \
       gmp-devel \
       mpfr-devel \
       libmpc-devel \
       nasm \
       m4 \
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
       rh-python36 \
       help2man \
       autoconf-archive \
    && yum clean all \
    && wget -O /tmp/autoconf-2.69.tar.gz --no-check-certificate --quiet https://ftp.gnu.org/gnu/autoconf/autoconf-2.69.tar.gz \
    && tar -zxf /tmp/autoconf-2.69.tar.gz -C /tmp \
    && pushd /tmp/autoconf-2.69 \
    && ./configure --prefix=/usr \
    && make -s \
    && make install \
    && popd \
    && rm -rf /tmp/autoconf-2.69* \
    && wget -O /tmp/automake-1.16.tar.gz --no-check-certificate --quiet https://ftp.gnu.org/gnu/automake/automake-1.16.tar.gz \
    && tar -zxf /tmp/automake-1.16.tar.gz -C /tmp \
    && pushd /tmp/automake-1.16 \
    && ./configure --prefix=/usr \
    && sed -i "s/'none';/'reduce';/g" bin/automake.in \
    && make -s \
    && make install \
    && popd \
    && rm -rf /tmp/automake-1.16* \
    && wget -O /tmp/cmake-3.14.3-Linux-x86_64.sh --no-check-certificate --quiet 'https://cmake.org/files/v3.14/cmake-3.14.3-Linux-x86_64.sh' \
    && bash /tmp/cmake-3.14.3-Linux-x86_64.sh --prefix=/usr/local --exclude-subdir \
    && rm /tmp/cmake-3.14.3-Linux-x86_64.sh \
    && pip install -q --upgrade --no-cache-dir pip \
    && pip install -q --no-cache-dir conan conan-package-tools \
    && sed -i 's/# %wheel/%wheel/g' /etc/sudoers \
    && groupadd 1001 -g 1001 \
    && useradd -ms /bin/bash conan -g 1001 -G wheel \
    && printf "conan:conan" | chpasswd \
    && chgrp -R wheel /opt/rh/rh-python36/root \
    && chmod -R g+w -R /opt/rh/rh-python36/root

# Fix sudo with arguments: https://bugzilla.redhat.com/show_bug.cgi?id=1319936
COPY sudo /opt/rh/devtoolset-7/root/usr/bin/sudo
RUN chmod a+x /opt/rh/devtoolset-7/root/usr/bin/sudo

USER conan
WORKDIR /home/conan
