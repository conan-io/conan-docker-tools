FROM conanio/gcc5

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends software-properties-common \
    && sudo add-apt-repository ppa:deadsnakes/ppa -y \
    && sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends \
    python-software-properties \
    python3.5 \
    python3.6 \
    python3.7 \
    python3.8 \
    python-setuptools \
    python-dev \
    python3.5-dev \
    python3.6-dev \
    python3.7-dev \
    python3.8-dev \
    python3.8-distutils \
    golang \
    pkg-config \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo ln -sf /usr/bin/python3.8 /usr/bin/python \
    && sudo ln -sf /usr/bin/python3.8 /usr/bin/python3 \
    && wget --no-check-certificate --quiet -O /tmp/get-pip.py https://bootstrap.pypa.io/get-pip.py \
    && sudo python3.8 /tmp/get-pip.py \
    && sudo python3.8 -m pip install --upgrade pip \
    && sudo python3.8 -m pip install "virtualenv<20.0.0" \
    && sudo python3.8 -m pip install PyGithub \
    && sudo python3.8 -m pip install meson

USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
