FROM conanio/gcc54

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends software-properties-common \
    && sudo add-apt-repository ppa:deadsnakes/ppa -y \
    && sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends \
    python-software-properties \
    python3.4 \
    python3.5 \
    python3.6 \
    python3.7 \
    python-setuptools \
    python-dev \
    python3.4-dev \
    python3.5-dev \
    python3.6-dev \
    python3.7-dev \
    golang \
    pkg-config \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo pip install --upgrade pip \
    && cd /tmp && wget https://bootstrap.pypa.io/get-pip.py \
    && sudo python3 get-pip.py \
    && sudo pip3 install "meson" \
    && sudo pip install virtualenv

USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
