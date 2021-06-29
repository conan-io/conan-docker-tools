import os
import subprocess
import uuid
from contextlib import contextmanager


class DockerContainer:
    def __init__(self, image, tmpfolder=None):
        self.image = image
        self.name = str(uuid.uuid4())
        self._tmpfolder = tmpfolder
        self.tmp = '/home/conan/build'
        self._working_dir = None

    def run(self):
        mount_volume = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'workingdir'))
        args = ["docker", "run", "-t", "-d", "-v", f"{mount_volume}:/home/conan/workingdir:ro"]
        if self._tmpfolder:
            args += ["-v", f"{self._tmpfolder}:{self.tmp}:rw"]
        args += ["--name", self.name, self.image]
        print(f'>> {" ".join(args)}')
        subprocess.check_call(args)

        self.exec(['sudo', 'chown', '-R', 'conan:1001', '/home/conan'])

    @contextmanager
    def working_dir(self, working_dir=None):
        wdir = working_dir or os.path.join('/home/conan', str(uuid.uuid4()))
        try:
            out, err = self.exec(['id'])
            print(out)
            print(err)
            out, err = self.exec(['id', '-u'])
            print(out)
            print(err)
            out, err = self.exec(['id', '-G'])
            print(out)
            print(err)

            out, err = self.exec(['ls', '-la', '/home'])
            print(out)
            print(err)

            out, err = self.exec(['ls', '-la', '/home/conan'])
            print(out)
            print(err)

            out, err = self.exec(['ls', '-la', '/home/conan/build'])
            print(out)
            print(err)

            self.exec(['mkdir', '-p', wdir])
            self._working_dir = wdir
            yield
        finally:
            self._working_dir = None

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
def run_container(image, tmpdirname):
    container = DockerContainer(image, tmpdirname)
    try:
        container.run()
        yield container
    finally:
        container.stop()
