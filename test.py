"""Execute image test by compiler version"""
from os import getenv
from os import system
from os.path import join


if __name__ == "__main__":
    COMPILER_VERSION = getenv("CONAN_COMPILER_VERSION")
    COMPILER_NAME = getenv("CONAN_COMPILER_NAME")

    DIR_NAME = "%s_%s" % (COMPILER_NAME, COMPILER_VERSION)
    TEST_PATH = join(DIR_NAME, "test.sh")
    system(TEST_PATH)
