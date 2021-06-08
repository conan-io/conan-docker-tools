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
        logging.info("Starting test: System")
        subprocess.check_call(["docker", "run", "-t", "-d", "-v", "%s:/tmp/project" % pwd, "--name", container, image])

        subprocess.check_call(["docker", "exec", container, "conan", "config", "init", "--force"])
        subprocess.check_call(["docker", "exec", container, "conan", "config", "set", "general.sysrequires_mode=enabled"])

        subprocess.check_call(["docker", "exec", container, "sudo", "cp", "/tmp/project/test/system/sources.list", "/etc/apt/sources.list"])
        subprocess.check_call(["docker", "exec", container, "sudo", "apt-key", "adv", "--keyserver", "keyserver.ubuntu.com", "--recv-keys", "60C317803A41BA51845E371A1E9377A2BA9EF27F"])
        subprocess.check_call(["docker", "exec", container, "sudo", "apt-get", "-qq", "update"])
        subprocess.check_call(["docker", "exec", container, "sudo", "apt-get", "-qq", "install", "-y", "--force-yes", "--no-install-recommends", "--no-install-suggests", "-o=Dpkg::Use-Pty=0", "g++-9"])
        subprocess.check_call(["docker", "exec", container, "mkdir", "/tmp/build"])

        subprocess.check_call(["docker", "exec", "-w", "/tmp/build", container, "conan", "install", "/tmp/project/test/system", "--build"])
        subprocess.check_call(["docker", "exec", "-w", "/tmp/build", container, "cmake", "/tmp/project/test/system", "-DCMAKE_BUILD_TYPE=Release"])
        subprocess.check_call(["docker", "exec", "-w", "/tmp/build", container, "cmake", "--build", "."])

        output = subprocess.check_output(["docker", "exec", "-w", "/tmp/build", container, "ldd", "bin/package_test"]).decode()
        if 'libstdc++.so.6 => /usr/local/lib64/libstdc++.so.6' not in output:
            raise RuntimeError("Could not find libstdc++.so.6 in package_test dependencies tree.")
        if 'libgcc_s.so.1 => /usr/local/lib64/libgcc_s.so.1' not in output:
            raise RuntimeError("Could not find libgcc_s.so.1 in package_test dependencies tree.")

        logging.info("Test result (System): SUCCESS")
    except Exception as error:
        logging.error("Test result (System): FAILURE - {}".format(error))
        exit_code = 1
    finally:
        subprocess.check_call(["docker", "stop", container])
        subprocess.check_call(["docker", "rm", "-f", container])

    sys.exit(exit_code)
