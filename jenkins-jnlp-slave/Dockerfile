ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE

ARG AGENT_VERSION=3.27

COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /opt/entrypoint.sh
COPY openjdk.list /etc/apt/sources.list.d/openjdk.list

RUN sudo apt-get update

RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DA1A4A13543B466853BAF164EB9B1D8886F44E2A \
    && sudo apt-get update \
    && sudo apt-get install -y --no-install-recommends openjdk-8-jre-headless curl \
    && sudo apt-get -qq clean -y \
    && sudo rm -rf /var/lib/apt/lists/* \
    && sudo rm -f /var/cache/apt/*.bin

RUN pip install --no-cache virtualenv \
    && sudo curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar \
    && sudo chmod 755 /usr/share/jenkins \
    && sudo chmod 644 /usr/share/jenkins/slave.jar \
    && sudo chmod +x /opt/entrypoint.sh /usr/local/bin/jenkins-slave

ENTRYPOINT ["/opt/entrypoint.sh"]
