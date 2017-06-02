from variables import Variables


class Image(object):

    def __init__(self, compiler_name, compiler_version):
        variables = Variables()
        self.__name = "%s/conan%s%s" % (variables.docker_username, compiler_name, compiler_version.replace(".", ""))
        self.__build_dir = "%s_%s" % (compiler_name, compiler_version)
        self.__compiler = compiler_name
        self.__version = compiler_version

    @property
    def name(self):
        return self.__name

    @property
    def build_dir(self):
        return self.__build_dir

    @property
    def version(self):
        return self.__version

    @property
    def compiler(self):
        return self.__compiler
