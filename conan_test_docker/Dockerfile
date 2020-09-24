FROM conanio/gcc5

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends \
    software-properties-common \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    && sudo add-apt-repository ppa:deadsnakes/ppa -y \
    && sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends \
    python-software-properties \
    python3.4 \
    python3.5 \
    python3.6 \
    python3.7 \
    python3.8 \
    python-setuptools \
    python-dev \
    python3.4-dev \
    python3.5-dev \
    python3.6-dev \
    python3.7-dev \
    python3.8-dev \
    python3.8-distutils \
    golang \
    pkg-config \
    && curl -kfsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - \
    && sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
    && sudo apt-get update \
    && sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
    && sudo apt-get remove -y software-properties-common apt-transport-https ca-certificates curl gnupg-agent \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo usermod -aG docker conan \
    && sudo pip install --upgrade pip \
    && cd /tmp && wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py \
    && sudo python3 get-pip.py \
    && sudo pip install "virtualenv<20.0.0" \
    && pip3 install PyGithub \
    && pip3 install meson \
    && pip3 install docker-compose \
    && sudo systemctl enable docker


USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
