import os
import subprocess
import uuid
from contextlib import contextmanager


class DockerContainer:
    def __init__(self, image, tmpfolder=None):
        self.image = image
        self.name = str(uuid.uuid4())
        self._tmpfolder = tmpfolder
        self.tmp = '/tmp/build'
        self._working_dir = None

    def _subproces(self, args):
        print(f'>> {" ".join(args)}')
        process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def run(self):
        mount_volume = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'workingdir'))
        args = ["docker", "run", "-t", "-d", "-v", f"{mount_volume}:/tmp/workingdir"]
        if self._tmpfolder:
            args += ["-v", f"{self._tmpfolder}:{self.tmp}"]
        args += ["--name", self.name, self.image, '/bin/bash']  # Add '/bin/bash' just in case it has some entry-point
        return self._subproces(args)

    @contextmanager
    def working_dir(self, working_dir=None):
        wdir = working_dir or os.path.join('/tmp', str(uuid.uuid4()))
        try:
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
        return self._subproces(args)

    def raw_exec(self, command: str, shell=True):
        wdir = f" -w {self._working_dir}" if self._working_dir else ''
        cmd = f"docker exec {wdir} {self.name} {command}"
        print(f'>> {cmd}')
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8'), stderr.decode('utf-8')

    def stop(self):
        subprocess.check_call(["docker", "stop", self.name])
        subprocess.check_call(["docker", "rm", "-f", self.name])


@contextmanager
def run_container(image, tmpdirname):
    container = DockerContainer(image, tmpdirname)
    try:
        container.run()
        yield container
    finally:
        container.stop()
