FROM i386/centos:6
ENTRYPOINT ["linux32", "--"]

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ENV PATH=/opt/pyenv/shims:/opt/rh/devtoolset-7/root/usr/bin:${PATH:+:${PATH}} \
    MANPATH=/opt/rh/devtoolset-7/root/usr/share/man${MANPATH:+:${MANPATH}} \
    INFOPATH=/opt/rh/devtoolset-7/root/usr/share/info${INFOPATH:+:${INFOPATH}} \
    PCP_DIR=/opt/rh/devtoolset-7/root \
    PERL5LIB=/opt/rh/devtoolset-7/root//usr/lib64/perl5/vendor_perl:/opt/rh/devtoolset-7/root/usr/lib/perl5:/opt/rh/devtoolset-7/root//usr/share/perl5/vendor_perl${PERL5LIB:+:${PERL5LIB}} \
    LD_LIBRARY_PATH=/opt/rh/devtoolset-7/root/usr/lib64:/opt/rh/devtoolset-7/root/usr/lib:/opt/rh/devtoolset-7/root/usr/lib64/dyninst:/opt/rh/devtoolset-7/root/usr/lib/dyninst${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}} \
    PYENV_ROOT=/opt/pyenv \
    CXX=/opt/rh/devtoolset-7/root/usr/bin/g++ \
    CC=/opt/rh/devtoolset-7/root/usr/bin/gcc

COPY cloudlinux.repo /etc/yum.repos.d/cloudlinux.repo

RUN printf "i686" >  /etc/yum/vars/arch \
    && printf "i386" >  /etc/yum/vars/basearch \
    && yum update -y \
    && yum install -y \
       sudo \
       wget \
       make \
       glibc-devel \
       gmp-devel \
       mpfr-devel \
       libmpc-devel \
       nasm \
       m4 \
       libffi-devel \
       pkgconfig \
       subversion \
       xz \
       curl \
       xz-devel \
       tar \
       devtoolset-7-toolchain \
       zlib-devel \
       bzip2 \
       bzip2-devel \
       readline-devel \
       sqlite \
       sqlite-devel \
       tk-devel \
       libffi-devel \
       libtool \
       perl-core \
       help2man \
       autoconf-archive \
       gettext \
       libcurl-devel \
    && yum clean all \
    && wget -O /tmp/git-2.22.0.tar.gz --no-check-certificate --quiet https://www.kernel.org/pub/software/scm/git/git-2.22.0.tar.gz \
    && tar -zxf /tmp/git-2.22.0.tar.gz -C /tmp \
    && pushd /tmp/git-2.22.0 \
    && ./configure --prefix=/usr --without-tcltk --with-curl \
    && make -s \
    && make install \
    && yum remove -y gettext libcurl-devel \
    && popd \
    && rm -rf /tmp/git-* \
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
    && wget --quiet -O /tmp/OpenSSL_1_0_2q.tar.gz https://github.com/openssl/openssl/archive/OpenSSL_1_0_2q.tar.gz \
    && tar zxf /tmp/OpenSSL_1_0_2q.tar.gz -C /tmp \
    && pushd /tmp/openssl-OpenSSL_1_0_2q \
    && ./Configure --prefix=/usr shared zlib linux-generic32 \
    && make -j`nproc` > /dev/null \
    && make install > /dev/null \
    && popd \
    && rm -rf /tmp/openssl-* /tmp/OpenSSL* \
    && wget --no-check-certificate --quiet -O /tmp/pyenv-installer https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer \
    && chmod +x /tmp/pyenv-installer \
    && /tmp/pyenv-installer \
    && rm /tmp/pyenv-installer \
    && update-alternatives --install /usr/bin/pyenv pyenv /opt/pyenv/bin/pyenv 100 \
    && pyenv install 3.6.7 \
    && pyenv global 3.6.7 \
    && update-alternatives --install /usr/bin/python python /opt/pyenv/shims/python 100 \
    && update-alternatives --install /usr/bin/python3 python3 /opt/pyenv/shims/python3 100 \
    && update-alternatives --install /usr/bin/pip pip /opt/pyenv/shims/pip 100 \
    && update-alternatives --install /usr/bin/pip3 pip3 /opt/pyenv/shims/pip3 100 \
    && pip install -q --upgrade --no-cache-dir pip scikit-build \
    && pip install -q --no-cache-dir conan conan-package-tools cmake==3.16.* \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir conan \
    && sed -i 's/# %wheel/%wheel/g' /etc/sudoers \
    && groupadd 1001 -g 1001 \
    && useradd -ms /bin/bash conan -g 1001 -G wheel \
    && printf "conan:conan" | chpasswd \
    && chown -R conan:1001 /opt/pyenv \
    && find /opt/pyenv -iname __pycache__ -print0 | xargs -0 rm -rf

# Fix sudo with arguments: https://bugzilla.redhat.com/show_bug.cgi?id=1319936
COPY sudo /opt/rh/devtoolset-7/root/usr/bin/sudo
RUN chmod a+x /opt/rh/devtoolset-7/root/usr/bin/sudo

USER conan
WORKDIR /home/conan

RUN mkdir -p /home/conan/.conan \
    && printf 'eval "$(pyenv init -)"\n' >> ~/.bashrc \
    && printf 'eval "$(pyenv virtualenv-init -)"\n' >> ~/.bashrc
