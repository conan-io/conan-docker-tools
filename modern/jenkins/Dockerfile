ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE as base

ARG JENKINS_AGENT_VERSION
ARG JAVA_JDK_VERSION=8

USER root

COPY jenkins-client /usr/local/bin/jenkins-client
COPY entrypoint.sh /opt/entrypoint.sh
COPY install-openjdk-ppa.sh /tmp/install-openjdk-ppa.sh
COPY cacert /etc/ssl/certs/java/cacerts

# INFO: OpenJDK11 wants cacert but is not installed and the Keystore type is not the expected: https://stackoverflow.com/questions/6784463/error-trustanchors-parameter-must-be-non-empty

RUN /tmp/install-openjdk-ppa.sh \
    && apt-get -qq update \
    && apt-get -q install -y openjdk-${JAVA_JDK_VERSION}-jre-headless curl \
    && /var/lib/dpkg/info/ca-certificates-java.postinst configure \
    && apt-get -q clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/*.bin \
    && pip3 install --no-cache virtualenv \
    && curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${JENKINS_AGENT_VERSION}/remoting-${JENKINS_AGENT_VERSION}.jar \
    && chmod 755 /usr/share/jenkins \
    && chmod 644 /usr/share/jenkins/slave.jar \
    && chmod +x /opt/entrypoint.sh /usr/local/bin/jenkins-client

ENTRYPOINT ["/opt/entrypoint.sh"]
USER conan
