import subprocess
from image import Image


class Build(object):
    """Base builder for docker image
    """

    def run(self, image):
        """Build docker image
        """
        subprocess.check_call("sudo docker build --no-cache -t %s %s" % (image.name, image.build_dir), shell=True)
