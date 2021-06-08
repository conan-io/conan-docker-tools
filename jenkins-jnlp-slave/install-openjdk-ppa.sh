#!/bin/sh

set -e

DISTRIB_CODENAME=`grep -oP 'DISTRIB_CODENAME=\K(.*)' /etc/lsb-release`
case $DISTRIB_CODENAME in
trusty|precise)
  echo "deb http://ppa.launchpad.net/openjdk-r/ppa/ubuntu ${DISTRIB_CODENAME} main" > /etc/apt/sources.list.d/openjdk.list
  apt-get -qq update
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DA1A4A13543B466853BAF164EB9B1D8886F44E2A
;;
esac
