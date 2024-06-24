ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE as base

ARG JAVA_JDK_VERSION=17

USER root

COPY install-openjdk-ppa.sh /tmp/install-openjdk-ppa.sh

RUN /tmp/install-openjdk-ppa.sh

RUN apt-get -qq update \
    && apt-get -q install -y openjdk-${JAVA_JDK_VERSION}-jre-headless  curl \
    && apt-get -q clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -f /var/cache/apt/*.bin

COPY jenkins-client /usr/local/bin/jenkins-client
COPY entrypoint.sh /opt/entrypoint.sh

ARG JENKINS_AGENT_VERSION

ADD --chown="conan":"conan" "https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${JENKINS_AGENT_VERSION}/remoting-${JENKINS_AGENT_VERSION}.jar" /usr/share/jenkins/agent.jar

RUN chmod 755 /usr/share/jenkins \
    && chmod 0644 /usr/share/jenkins/agent.jar \
    && chmod +x /opt/entrypoint.sh /usr/local/bin/jenkins-client \
    && ln -sf /usr/share/jenkins/agent.jar /usr/share/jenkins/slave.jar \
    && ln -sf /usr/local/bin/jenkins-client /usr/local/bin/jenkins-agent \
    && ln -sf /usr/local/bin/jenkins-client /usr/local/bin/jenkins-slave

ARG CONAN_VERSION

RUN pip3 install --no-cache conan==${CONAN_VERSION} virtualenv

ENTRYPOINT ["/opt/entrypoint.sh"]
USER conan
