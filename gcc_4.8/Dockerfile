FROM gcc:4.8

MAINTAINER Luis Martinez de Bartolome

RUN apt-get update && apt-get install -y python-dev sudo
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
RUN wget https://bootstrap.pypa.io/get-pip.py && python get-pip.py && pip install -U pip
RUN pip install conan
RUN groupadd 1001 -g 1001
RUN useradd -ms /bin/bash conan -g 1001
USER conan
WORKDIR /home/conan
RUN mkdir -p /home/conan/.conan
