ARG JENKINS_BRANCH=apt
ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE as base

ARG JENKINS_AGENT_VERSION
ARG JAVA_JDK_VERSION=11

USER root

COPY jenkins-client /usr/local/bin/jenkins-client
COPY entrypoint.sh /opt/entrypoint.sh

FROM base AS branch-apt

COPY install-openjdk-ppa.sh /tmp/install-openjdk-ppa.sh

RUN /tmp/install-openjdk-ppa.sh \
    && apt-get -qq update \
    && apt-get -q install -y openjdk-8-jre-headless

FROM base AS branch-download

COPY install-adopt-openjdk-ppa.sh /tmp/install-adopt-openjdk-ppa.sh

RUN /tmp/install-adopt-openjdk-ppa.sh \
    && apt-get -qq update \
    && apt-get -q install -y adoptopenjdk-${JAVA_JDK_VERSION}-jre-hotspot-set-default

FROM branch-${JENKINS_BRANCH} as final
RUN apt-get -qq update \
    && apt-get -q install -y curl \
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
