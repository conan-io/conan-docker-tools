ARG SOURCE_CONANIO_IMAGE

#Usage: docker build <docker image name> --build-arg SOURCE_CONANIO_IMAGE=<conanio dockerhub image> .
FROM $SOURCE_CONANIO_IMAGE

USER root

ARG AGENT_VERSION=3.27

#Copy scripts
COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /entrypoint.sh

#Installing required packages
RUN yum install -y \
    java-1.8.0-openjdk \
    curl \
    && yum clean all \
    && pip install --no-cache virtualenv \
    && curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar \
    && chmod +x /entrypoint.sh \
    && chmod +x /usr/local/bin/jenkins-slave \
    && chmod 755 /usr/share/jenkins \
    && chmod 644 /usr/share/jenkins/slave.jar

#Setting entrypoint
ENTRYPOINT ["/entrypoint.sh"]

USER conan
