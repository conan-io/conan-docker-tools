#!/bin/sh

set -e

DISTRIB_CODENAME=`grep -oP 'DISTRIB_CODENAME=\K(.*)' /etc/lsb-release`
case $DISTRIB_CODENAME in
xenial|trusty|precise)
  echo "deb http://ppa.launchpad.net/openjdk-r/ppa/ubuntu ${DISTRIB_CODENAME} main" > /etc/apt/sources.list.d/openjdk.list
  apt-get -qq update
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys DA1A4A13543B466853BAF164EB9B1D8886F44E2A
;;
eoan)
  # eoan is not supported by the openjdk-r/ppa repository
  # openjdk-14 is the latest version available in the eoan repository, so we use xenial
  sed -i -E 's/python3/python3.7/g' /usr/bin/add-apt-repository
  add-apt-repository --yes ppa:openjdk-r/ppa
  add-apt-repository --yes 'deb https://ppa.launchpadcontent.net/openjdk-r/ppa/ubuntu xenial main'
;;
esac
