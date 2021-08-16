FROM mcr.microsoft.com/dotnet/framework/sdk:4.8


LABEL maintainer="Conan.io <info@conan.io>"

SHELL ["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command"]

ARG CONAN_VERSION

ENV chocolateyUseWindowsCompression=false \
    PYTHONIOENCODING=UTF-8

RUN iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1')); \
    $env:Path += '";C:\tools\python3;C:\tools\python3\Scripts"'; \
    choco install --no-progress --yes git --version=2.32.0.2 --params '"/InstallDir:C:\tools\git"'; \
    choco install --no-progress --yes svn --version=1.8.17 --params '"/InstallDir:C:\tools\svn"'; \
    choco install --no-progress --yes cmake --version=3.21.0 --params '"/InstallDir:C:\tools\cmake"' --installargs 'ADD_CMAKE_TO_PATH=""System""'; \
    choco install --no-progress --yes python3 --version=3.7.9 --params '"/InstallDir:C:\tools\python3"'

RUN choco install --no-progress --yes --ignore-package-exit-codes=3010 dotnetfx --version=4.8.0.20190930
RUN choco install --no-progress --yes  --ignore-package-exit-codes=-2147024770 visualstudio2019buildtools --version=16.10.4.0
RUN choco install --yes visualstudio2019-workload-vctools --version=1.0.1
RUN choco install --no-progress --yes --execution-timeout=0 visualstudio2019-workload-manageddesktop --version=1.0.2
RUN choco install --no-progress --yes windows-sdk-10.1 --version=10.1.18362.1

RUN python -m pip install --quiet --upgrade pip; \
    python -m pip install win-unicode-console --quiet --upgrade --force-reinstall --no-cache; \
    python -m pip install conan==${CONAN_VERSION} --quiet --upgrade --force-reinstall --no-cache; \
    python -m conan config init

WORKDIR "C:/Users/ContainerAdministrator"
ENTRYPOINT ["cmd.exe", "C:\\Program Files (x86)\\Microsoft Visual C++ Build Tools\\vcbuildtools_msbuild.bat"]
