ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE

USER root

ARG AGENT_VERSION=3.27

COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /entrypoint.sh
COPY install-openjdk-ppa.sh /tmp/install-openjdk-ppa.sh

#Install java to launch slave.jar
RUN /tmp/install-openjdk-ppa.sh &&\
    apt-get -qq update &&\
    apt-get install -q -y openjdk-8-jre-headless curl &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    pip3 install --no-cache virtualenv &&\
    curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar &&\
    chmod 755 /usr/share/jenkins &&\
    chmod 644 /usr/share/jenkins/slave.jar &&\
    chmod +x /entrypoint.sh /usr/local/bin/jenkins-slave

#Setting entrypoint
ENTRYPOINT ["/entrypoint.sh"]

USER conan