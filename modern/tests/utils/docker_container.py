import os
import subprocess
import uuid
from contextlib import contextmanager


class DockerContainer:
    def __init__(self, image, volumes_from, user=None):
        self.image = image
        self.name = str(uuid.uuid4())
        self._volumes_from = volumes_from
        self._user = user
        # Assume working_dir is the root of the repository
        self._working_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

    def run(self):
        args = ["docker", "run", "-t", "-d", "--name", self.name]
        if self._user:
            args += ["-u", self._user]
        if self._volumes_from:
            args += ["--volumes-from", self._volumes_from]
        else:
            mount_volume = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
            args += ["-v", f"{mount_volume}:{self._working_dir}:rw"]
        args += [self.image, ]

        # If it is the Jenkins image, we need to modify the entrypoint
        if '-jenkins:' in self.image:
            args += ['/bin/bash', ]

        print(f'>> {" ".join(args)}')
        subprocess.check_call(args)

    @contextmanager
    def working_dir(self, working_dir=''):
        old_wdir = self._working_dir
        try:
            wdir = os.path.join(self._working_dir, working_dir)
            self.exec(['mkdir', '-p', wdir])
            self._working_dir = wdir
            yield
        finally:
            self._working_dir = old_wdir

    def bash(self, bash_commands: list):
        return self.exec(['/bin/bash', ] + bash_commands)

    def exec(self, commands: list):
        args = ["docker", "exec"]
        if self._working_dir:
            args += ["-w", self._working_dir]
        args += [self.name, ] + commands
        print(f'>> {" ".join(args)}')
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if stderr:
            print(f'ERROR: {stderr.decode("utf-8")}')
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def stop(self):
        subprocess.call(["docker", "stop", self.name])
        subprocess.check_call(["docker", "rm", "-f", self.name])

    @contextmanager
    def run_container(self, image):
        with run_container(image, self._volumes_from, self._user) as container:
            yield container


@contextmanager
def run_container(image, volumes_from, user):
    container = DockerContainer(image, volumes_from, user)
    try:
        container.run()
        yield container
    finally:
        container.stop()
