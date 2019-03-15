ARG SOURCE_CONANIO_IMAGE

#Usage: docker build <docker image name> --build-arg SOURCE_CONANIO_IMAGE=<conanio dockerhub image> .
FROM $SOURCE_CONANIO_IMAGE

USER root

ARG AGENT_VERSION=3.27

#Install java to launch slave.jar
RUN apt-get -q update &&\
    apt-get install -y openjdk-8-jre-headless curl &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    pip3 install virtualenv

#Installing slave.jar
RUN curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar \
  && chmod 755 /usr/share/jenkins \
  && chmod 644 /usr/share/jenkins/slave.jar

#Copy scripts
COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh /usr/local/bin/jenkins-slave

#Setting entrypoint
ENTRYPOINT ["/entrypoint.sh"]

USER conan