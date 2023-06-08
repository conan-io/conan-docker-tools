ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE as base

ARG AGENT_VERSION
ARG CONAN_VERSION
ARG JAVA_JDK_VERSION=8

USER root

COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /opt/entrypoint.sh
COPY install-openjdk-ppa.sh /tmp/install-openjdk-ppa.sh

RUN /tmp/install-openjdk-ppa.sh \
    && apt-get -qq update \
    && apt-get -q install -y openjdk-${JAVA_JDK_VERSION}-jre-headless  curl \
    && apt-get -q clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/*.bin \
    && pip3 install --no-cache conan==${CONAN_VERSION} virtualenv \
    && curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar \
    && chmod 755 /usr/share/jenkins \
    && chmod 644 /usr/share/jenkins/slave.jar \
    && chmod +x /opt/entrypoint.sh /usr/local/bin/jenkins-slave

ENTRYPOINT ["/opt/entrypoint.sh"]
USER conan
