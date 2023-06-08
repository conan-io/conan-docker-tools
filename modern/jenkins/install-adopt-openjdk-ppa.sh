#!/bin/sh

set -e

DISTRIB_CODENAME=`grep -oP 'DISTRIB_CODENAME=\K(.*)' /etc/lsb-release`
case $DISTRIB_CODENAME in
xenial|trusty|precise)
  echo "deb http://ppa.launchpad.net/rpardini/adoptopenjdk/ubuntu ${DISTRIB_CODENAME} main" > /etc/apt/sources.list.d/openjdk.list
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D8533594C2DEDF3E
  apt-get -qq update
;;
esac
