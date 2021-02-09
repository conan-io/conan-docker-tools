FROM conanio/gcc5

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends software-properties-common \
    && sudo add-apt-repository ppa:deadsnakes/ppa -y \
    && sudo apt-get update \
    && sudo apt-get -qq install -y --no-install-recommends \
    golang \
    pkg-config \
    && sudo rm -rf /var/lib/apt/lists/*

RUN PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 2.7.16 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.5.7 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.6.9 \
    && PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.8.1 \
    && pyenv global 3.8.1

RUN python --version \
    && pip --version \
    && python -m pip install --upgrade pip \
    && python -m pip install "virtualenv<20.0.0" PyGithub meson conan

USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
