ARG JENKINS_BRANCH=apt
ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE as base

ARG AGENT_VERSION
ARG CONAN_VERSION
ARG JAVA_JDK_VERSION=11

USER root

COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /opt/entrypoint.sh

FROM base AS branch-apt

COPY install-openjdk-ppa.sh /tmp/install-openjdk-ppa.sh

RUN /tmp/install-openjdk-ppa.sh \
    && apt-get -qq update \
    && apt-get -q install -y openjdk-8-jre-headless

FROM base AS branch-download
RUN wget -q --no-check-certificate https://download.java.net/java/ga/jdk${JAVA_JDK_VERSION}/openjdk-${JAVA_JDK_VERSION}_linux-x64_bin.tar.gz -O /tmp/openjdk.tar.gz \
    && mkdir -p /opt/openjdk \
    && tar -xzf /tmp/openjdk.tar.gz -C /opt/openjdk --strip-components=1 \
    && sudo update-alternatives --install /usr/bin/java java /opt/openjdk/bin/java 100 \
    && rm -rf /tmp/openjdk.tar.gz

ENV JAVA_HOME=/opt/openjdk
ENV PATH="$PATH:$JAVA_HOME/bin"

FROM branch-${JENKINS_BRANCH} as final

RUN apt-get -qq update \
    && apt-get -q install -y curl \
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
