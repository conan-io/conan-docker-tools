FROM lasote/conangcc63

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN sudo apt-get update && sudo apt install -y xz-utils liblzma-dev
RUN wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz && tar xf Python-3.7.0.tar.xz
RUN cd Python-3.7.0 && ./configure && sudo make altinstall
RUN sudo pip uninstall -y conan
