class Compiler(object):
    """Base builder for docker image
    """
    def __init__(self, name, versions):
        self.__name = name
        self.__versions = versions

    @property
    def name(self):
        """Retrieve compiler name
        """
        return self.__name

    @property
    def versions(self):
        """Retrieve supported versions
        """
        return self.__versions


class GccCompiler(Compiler):
    """Specilized builder for GCC
    """
    def __init__(self):
        Compiler.__init__(self, "gcc", ["4.6", "4.8", "4.9", "5.2", "5.3", "5.4", "6.2", "6.3"])


class ClangCompiler(Compiler):
    """Specialized builder for Clang
    """
    def __init__(self):
        Compiler.__init__(self, "clang", ["3.8", "3.9", "4.0"])
