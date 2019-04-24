FROM python:3.7-alpine3.7

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ARG CONAN_VERSION
ENV CONAN_VERSION=${CONAN_VERSION}

ADD https://github.com/conan-io/conan/archive/${CONAN_VERSION}.zip /

RUN apk add --no-cache gcc libc-dev \
    && unzip ${CONAN_VERSION} \
    && rm ${CONAN_VERSION}.zip \
    && cd conan-${CONAN_VERSION} \
    && pip3 install -r conans/requirements.txt \
    && pip3 install -r conans/requirements_server.txt \
    && pip3 install gunicorn \
    && apk del gcc libc-dev \
    # Do not migrate anything!
    # Only populate ~/.conan_server with /data, server.conf and version.txt to avoid
    # issues in a first run with multiple workers.
    && PYTHONPATH=${PWD} python conans/conan_server.py --migrate

EXPOSE 9300

WORKDIR /conan-${CONAN_VERSION}

COPY entrypoint.sh .

CMD /conan-${CONAN_VERSION}/entrypoint.sh
