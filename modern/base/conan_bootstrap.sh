#!/bin/bash

set -ex

version=$(conan --version | awk '{print $1}')
major=$(awk '{print substr($0, 0, 1)}' <<< ${version})

if [[ "${major}" == "2" ]]
then
    CONAN_USER_HOME=/tmp/conan conan install -r conancenter -g deploy -of /opt/conan -l /opt/conan/conan.lock /opt/conan/conanfile.txt
    rm -rf /tmp/conan
else
    CONAN_REVISIONS_ENABLED=1 CONAN_USER_HOME=/tmp/conan conan install -r conancenter -g deploy -if /opt/conan -l /opt/conan/conan.lock /opt/conan/conanfile.txt
    rm -rf /tmp/conan
    conan config set general.revisions_enabled=1
fi
