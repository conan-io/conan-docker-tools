"""Execute image test by compiler version"""
import os
from os import path


if __name__ == "__main__":
    COMPILER_VERSION = os.getenv("CONAN_COMPILER_VERSION")
    COMPILER_NAME = os.getenv("CONAN_COMPILER_NAME")

    DIR_NAME = "%s_%s" % (COMPILER_NAME, COMPILER_VERSION)
    TEST_PATH = path.join(DIR_NAME, "test.sh")
    assert(os.system(TEST_PATH) == os.EX_OK)
