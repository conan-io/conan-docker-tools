from image import Image
from variables import Variables
import subprocess
import os
import sys


class Deploy(object):
    """Base builder for docker image
    """

    def run(self, image):
        """Build docker image
        """
        variables = Variables()
        result = subprocess.call(['sudo', 'docker', 'login', '-p', variables.docker_password, '-u', variables.docker_username], stderr=sys.stderr)
        if result != os.EX_OK:
            raise RuntimeError("Could not login username %s to Docker server" % variables.docker_username)
        subprocess.check_call("sudo docker push %s" % image.name, shell=True)
