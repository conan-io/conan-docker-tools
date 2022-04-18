#!/bin/bash

set -ex

pip install conan==$1
version=`conan --version | awk '{print $3}'`

if [[ "${version}" == 2.* ]]
then
    pip install conan==1.47.0
    CONAN_REVISIONS_ENABLED=1 CONAN_USER_HOME=/tmp/conan conan install -r conancenter -g deploy -if /opt/conan -l /opt/conan/conan.lock /opt/conan/conanfile.txt
    rm -rf /tmp/conan
    pip install conan==${version}
else
    CONAN_REVISIONS_ENABLED=1 CONAN_USER_HOME=/tmp/conan conan install -r conancenter -g deploy -if /opt/conan -l /opt/conan/conan.lock /opt/conan/conanfile.txt
    rm -rf /tmp/conan
    conan config set general.revisions_enabled=1
fi
