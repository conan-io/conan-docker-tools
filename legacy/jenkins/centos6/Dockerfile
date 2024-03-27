ARG SOURCE_CONANIO_IMAGE
FROM $SOURCE_CONANIO_IMAGE

ARG JENKINS_AGENT_VERSION=3206.vb_15dcf73f6a_9
USER root

COPY jenkins-client /usr/local/bin/jenkins-client
COPY entrypoint.sh /opt/entrypoint.sh

RUN yum install -y \
    java-1.8.0-openjdk \
    curl \
    && yum clean all \
    && pip install --no-cache virtualenv \
    && curl --create-dirs -sSLo /usr/share/jenkins/agent.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${JENKINS_AGENT_VERSION}/remoting-${JENKINS_AGENT_VERSION}.jar \
    && chmod +x /opt/entrypoint.sh \
    && chmod +x /usr/local/bin/jenkins-client \
    && chmod 755 /usr/share/jenkins \
    && chmod 644 /usr/share/jenkins/agent.jar

ENTRYPOINT ["/opt/entrypoint.sh"]
USER conan
