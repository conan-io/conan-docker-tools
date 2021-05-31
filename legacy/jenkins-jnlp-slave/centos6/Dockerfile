ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE

ARG AGENT_VERSION=3.27
USER root

COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /opt/entrypoint.sh

RUN yum install -y \
    java-1.8.0-openjdk \
    curl \
    && yum clean all \
    && pip install --no-cache virtualenv \
    && curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar \
    && chmod +x /opt/entrypoint.sh \
    && chmod +x /usr/local/bin/jenkins-slave \
    && chmod 755 /usr/share/jenkins \
    && chmod 644 /usr/share/jenkins/slave.jar

ENTRYPOINT ["/opt/entrypoint.sh"]
USER conan
