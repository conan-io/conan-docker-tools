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
        logging.info("Starting test: Clang (Internal)")
        subprocess.check_call(["docker", "run", "-t", "-d", "-v", "%s:/tmp/project" % pwd, "--name", container, image])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/test/clang/conan/test_conan.sh"])
        logging.info("Test result (Clang Internal): SUCCESS")
    except Exception as error:
        logging.error("Test result (Clang Internal): FAILURE - {}".format(error))
        exit_code = 1
    finally:
        subprocess.check_call(["docker", "stop", container])
        subprocess.check_call(["docker", "rm", "-f", container])

    if exit_code:
        sys.exit(exit_code)

    container = "ubuntu-" + str(random.randint(1, 9999))

    try:
        logging.info("Starting test: Clang (Vanilla)")
        subprocess.check_call(["docker", "run", "-t", "-d", "-v", "%s:/tmp/project" % pwd, "--name", container, "ubuntu:xenial"])

        subprocess.check_call(["docker", "exec", container, "cp", "/tmp/project/libllvm-unwind.so.1.0" "/usr/lib/x86_64-linux-gnu/libllvm-unwind.so.1"])
        subprocess.check_call(["docker", "exec", container, "cp", "/tmp/project/libllvm-unwind.so.1.0" "/usr/lib/x86_64-linux-gnu/libunwind.so.1"])
        subprocess.check_call(["docker", "exec", container, "cp", "/tmp/project/libc++.so.1.0" "/usr/lib/x86_64-linux-gnu/libc++.so.1"])
        subprocess.check_call(["docker", "exec", container, "cp", "/tmp/project/libc++abi.so.1.0" "/usr/lib/x86_64-linux-gnu/libc++abi.so.1"])
        subprocess.check_call(["docker", "exec", container, "cp", "/tmp/project/libstdc++.so.6.0.29" "/usr/lib/x86_64-linux-gnu/libstdc++.so.6.0.21"])
        subprocess.check_call(["docker", "exec", container, "cp", "/tmp/project/libatomic.so.1.2.0" "/usr/lib/x86_64-linux-gnu/libatomic.so.1"])

        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/foobar_cpp_libcpp"])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/foobar_c_libcpp"])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/foobar_cpp_libstdcpp"])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/foobar_c_libstdcpp"])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/foobar_cpp_libstdcpp11"])
        subprocess.check_call(["docker", "exec", container, "/bin/bash", "/tmp/project/foobar_c_libstdcpp11"])

        logging.info("Test result (Clang Vanilla): SUCCESS")
    except Exception as error:
        logging.error("Test result (Clang Vanilla): FAILURE - {}".format(error))
        exit_code = 1
    finally:
        subprocess.check_call(["docker", "stop", container])
        subprocess.check_call(["docker", "rm", "-f", container])

    sys.exit(exit_code)
