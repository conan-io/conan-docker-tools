#### How does Jenkins work with CDT?

There are 4 files on .ci/ folder:

* conan_center_index.jenkinsfile
* on_conan_release.jenkinsfile
* generate.jenkinsfile
* jenkinsfile


- All jobs are executed only on Linux node.


#### on_conan_release.jenkinsfile

- It's triggered by Conan client CI, as soon as a new release is available.
- The released Conan version is passed by Jenkins parameter
- It can start 2 main jobs, based on parameters passed by Jenkins environment:
  - build_old_images: Build legacy docker images.
  - build_new_images: Build modern Docker images. It runs conan_center_index file
- As last stage, it opens a new Github PR to CDT with updated .env file

#### jenkinsfile

- Load parameters from Jenkins to upload or not built docker images
- Parse .env file as parameters and run _generate

#### conan_center_index.jenkinsfile

- Generate a range of versions from the required version on CCI and the latest version available on Pypi
- Load parameters from .env file, including compiler versions
- Run _generate to build Docker images based on Conan versions

#### generate.jenkinsfile

- Build a modern image
- Upload when running on master branch
- Uses docker cache from Artifactory
