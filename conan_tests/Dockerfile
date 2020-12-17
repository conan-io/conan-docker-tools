FROM conanio/gcc5

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN sudo apt-get update
RUN sudo apt-get -qq install -y --no-install-recommends software-properties-common
RUN sudo add-apt-repository ppa:deadsnakes/ppa -y
RUN sudo apt-get update
RUN sudo apt-get -qq install -y --no-install-recommends python-software-properties
RUN sudo apt-get -qq install -y --no-install-recommends python3.4
RUN sudo apt-get -qq install -y --no-install-recommends python3.5
RUN sudo apt-get -qq install -y --no-install-recommends python3.6
RUN sudo apt-get -qq install -y --no-install-recommends python3.7
RUN sudo apt-get -qq install -y --no-install-recommends python3.8
RUN sudo apt-get -qq install -y --no-install-recommends python-setuptools
RUN sudo apt-get -qq install -y --no-install-recommends python-dev
RUN sudo apt-get -qq install -y --no-install-recommends python3.4-dev
RUN sudo apt-get -qq install -y --no-install-recommends python3.5-dev
RUN sudo apt-get -qq install -y --no-install-recommends python3.6-dev
RUN sudo apt-get -qq install -y --no-install-recommends python3.7-dev
RUN sudo apt-get -qq install -y --no-install-recommends python3.8-dev
RUN sudo apt-get -qq install -y --no-install-recommends python3.8-distutils
RUN sudo apt-get -qq install -y --no-install-recommends golang
RUN sudo apt-get -qq install -y --no-install-recommends pkg-config
RUN sudo rm -rf /var/lib/apt/lists/*
RUN sudo pip install --upgrade pip
RUN cd /tmp && wget https://bootstrap.pypa.io/get-pip.py
RUN sudo python3 /tmp/get-pip.py
RUN sudo pip install "virtualenv<20.0.0"
RUN pip3 install PyGithub
RUN pip3 install meson

USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
