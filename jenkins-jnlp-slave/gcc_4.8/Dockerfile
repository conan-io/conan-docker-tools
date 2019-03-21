ARG SOURCE_CONANIO_IMAGE

#Usage: docker build <docker image name> --build-arg SOURCE_CONANIO_IMAGE=<conanio dockerhub image> .
FROM $SOURCE_CONANIO_IMAGE

USER root

ARG AGENT_VERSION=3.27

#Copy scripts
COPY jenkins-slave /usr/local/bin/jenkins-slave
COPY entrypoint.sh /entrypoint.sh

#Install java to launch slave.jar
RUN apt-get -q update &&\
    apt-get install python2.7 -y &&\
    update-alternatives --install /usr/bin/python python /usr/bin/python2.7 101 &&\
    update-alternatives --auto python &&\
    apt-get install -y software-properties-common &&\
    sed -i '0,/python3/s//python3.4/' /usr/bin/add-apt-repository &&\
    add-apt-repository -y ppa:openjdk-r/ppa &&\
    apt-get -q update &&\
    apt-get install -y openjdk-8-jre-headless curl &&\
    apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f /var/cache/apt/*.bin &&\
    pip install virtualenv &&\
    curl --create-dirs -sSLo /usr/share/jenkins/slave.jar https://repo.jenkins-ci.org/public/org/jenkins-ci/main/remoting/${AGENT_VERSION}/remoting-${AGENT_VERSION}.jar &&\
    chmod 755 /usr/share/jenkins &&\
    chmod 644 /usr/share/jenkins/slave.jar &&\
    chmod +x /entrypoint.sh /usr/local/bin/jenkins-slave &&\
    update-alternatives --remove python /usr/bin/python2.7

#Setting entrypoint
ENTRYPOINT ["/entrypoint.sh"]

USER conan