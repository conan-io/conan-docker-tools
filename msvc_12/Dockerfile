FROM microsoft/windowsservercore:10.0.14393.2485

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

SHELL ["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command"]

ENV chocolateyUseWindowsCompression=false \
    PYTHONIOENCODING=UTF-8

RUN iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

RUN choco install --no-progress --yes git --version=2.19.0 --params '"/InstallDir:C:\tools\git"'
RUN choco install --no-progress --yes svn --version=1.8.17 --params '"/InstallDir:C:\tools\svn"'
RUN choco install --no-progress --yes cmake --version=3.12.2 --params '"/InstallDir:C:\tools\cmake"' --installargs 'ADD_CMAKE_TO_PATH=""System""'
RUN choco install --no-progress --yes python3 --version=3.7.0 --params '"/InstallDir:C:\tools\python3"'

RUN choco install --no-progress --yes microsoft-build-tools --version 12.0.21005.20140416
RUN choco install --no-progress --yes visualstudioexpress2013windows --version 12.0.21005.1

RUN RefreshEnv

RUN python -m pip install --quiet --upgrade pip
RUN pip install win-unicode-console --quiet --upgrade --force-reinstall --no-cache
RUN pip install conan --quiet --upgrade --force-reinstall --no-cache
RUN pip install conan_package_tools --quiet --upgrade --force-reinstall --no-cache

# FIXME (uilian): idna raises error when installed by Conan/CPT
RUN pip install idna --quiet --upgrade --force-reinstall --no-cache

WORKDIR "C:/Users/ContainerAdministrator"
ENTRYPOINT ["cmd.exe", "C:\\Program Files (x86)\\Microsoft Visual C++ Build Tools\\vcbuildtools_msbuild.bat"]
