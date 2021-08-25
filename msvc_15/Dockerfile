FROM mcr.microsoft.com/windows/servercore:ltsc2019

LABEL maintainer="Conan.io <info@conan.io>"

SHELL ["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command"]

ARG CONAN_VERSION

ENV chocolateyUseWindowsCompression=false \
    PYTHONIOENCODING=UTF-8

RUN iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')); \
    $env:Path += '";C:\tools\python3;C:\tools\python3\Scripts"';

RUN choco install --no-progress --yes git --version=2.32.0.2 --params '"/InstallDir:C:\tools\git"'
RUN choco install --no-progress --yes svn --version=1.8.17 --params '"/InstallDir:C:\tools\svn"'
RUN choco install --no-progress --yes cmake --version=3.21.0 --params '"/InstallDir:C:\tools\cmake"' --installargs 'ADD_CMAKE_TO_PATH=""System""'
RUN choco install --no-progress --yes python3 --version=3.7.9 --params '"/InstallDir:C:\tools\python3"'

RUN choco install --no-progress --yes  --ignore-detected-reboot --ignore-package-exit-codes=3010 dotnetfx --version=4.8.0.20190930
RUN choco install --no-progress --yes visualstudio2017buildtools --version=15.9.37.0 --ignore-detected-reboot

# FIXME: visualstudio2017-workload-vctools fails to install. Error code 1
# RUN choco install --yes visualstudio2017-workload-vctools --version=1.3.3 --ignore-detected-reboot --force --ignore-package-exit-codes=1 --use-package-exit-codes=0 || EXIT 0
RUN if ($(choco install --yes visualstudio2017-workload-vctools --version=1.3.3 --ignore-detected-reboot --force --ignore-package-exit-codes=1 --use-package-exit-codes=0; $null = $null; $?)) { 'success' }

RUN choco install --no-progress --yes --execution-timeout=0 visualstudio2017-workload-manageddesktop --version=1.2.3
RUN choco install --no-progress --yes windows-sdk-10.0 --version=10.0.26624

ENV PATH="C:\tools\python3;C:\tools\python3\Scripts;%PATH%"

RUN pip --version
RUN pip install --quiet --upgrade pip
RUN pip install win-unicode-console --quiet --upgrade --force-reinstall --no-cache-dir
RUN pip install conan==1.39.0 --quiet --upgrade --force-reinstall --no-cache-dir

SHELL ["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command"]

WORKDIR "C:/Users/ContainerAdministrator"
ENTRYPOINT ["cmd.exe", "C:\\Program Files (x86)\\Microsoft Visual C++ Build Tools\\vcbuildtools_msbuild.bat"]
