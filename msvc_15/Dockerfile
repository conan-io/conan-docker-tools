FROM conanio/msvcbase

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

RUN choco install --no-progress --yes visualstudio2017buildtools --version=15.8.2.0
RUN choco install --no-progress --yes visualstudio2017-workload-vctools --version=1.3.0
RUN choco install --no-progress --yes visualstudio2017-workload-manageddesktop --version=1.2.0
RUN RefreshEnv