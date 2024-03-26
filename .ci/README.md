#### How does Jenkins work with ConanDockerTools (CDT)?

There are 2 files on .ci/ folder:

* on_conan_release.jenkinsfile
* jenkinsfile


- All jobs are executed only on Linux node.


#### on_conan_release.jenkinsfile

- It's triggered by Conan client CI, as soon as a new release is available.
- The released Conan version is passed by Jenkins parameter
- It can start a main job, based on parameters passed by Jenkins environment
- The job splits in modern and legacy images versions
- As last stage, it opens a new Github PR to CDT with updated .env file

#### jenkinsfile

- Load parameters from Jenkins to upload or not built docker images
- Parse .env file as parameters
- Generate a range of versions to build listed in .env file
- Load parameters from .env file, including compiler versions
- Build Docker images based on Conan versions
- Upload when running on master branch
- Uses docker cache from Artifactory
