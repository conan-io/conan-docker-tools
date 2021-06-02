#!/usr/bin/env python
import re
import sys
import os
import subprocess
import random
import logging


def get_conan_target_version():
    env_file = open(".env", "r")
    match = re.search("CONAN_VERSION=(.*)", env_file.read())
    if not match:
        return "latest"
    return match.group(1)


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s [%(levelname)s]: %(message)s', level=logging.INFO)
    compiler = sys.argv[1]
    container = compiler + "-" + str(random.randint(1, 9999))
    pwd = os.getcwd()
    image = "{}/{}-ubuntu16.04:{}".format(os.getenv("DOCKER_USERNAME", "conanio"), compiler, get_conan_target_version())
    exit_code = 0

    try:
        logging.info("Starting test: Standard")
        subprocess.check_call(["docker", "run", "-t", "-d", "-v", "%s:/tmp/project" % pwd, "--name", container, image])
        subprocess.check_call(["docker", "exec", container, "git", "clone", "https://github.com/conan-io/conan-center-index.git"])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/test/standard/build_imagl.sh"])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/test/standard/build_libsolace.sh"])

        logging.info("Test result (Standard): SUCCESS")
    except Exception as error:
        logging.error("Test result (Standard): FAILURE - {}".format(error))
        exit_code = 1
    finally:
        subprocess.check_call(["docker", "stop", container])
        subprocess.check_call(["docker", "rm", "-f", container])

    sys.exit(exit_code)
