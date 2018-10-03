FROM microsoft/windowsservercore:10.0.14393.2068

LABEL maintainer="Luis Martinez de Bartolome <luism@jfrog.com>"

ADD https://aka.ms/vs/15/release/vs_buildtools.exe %TEMP%\buildtools.exe

RUN %TEMP%\buildtools.exe --quiet --wait --norestart --nocache \
    --installPath C:\BuildTools \
    --add Microsoft.VisualStudio.Workload.VCTools;includeRecommended  \
    --add Microsoft.VisualStudio.Component.VC.Tools.x86.x64 \
    --add Microsoft.VisualStudio.Component.Windows10SDK.17134 \
    --add Microsoft.VisualStudio.Component.Windows10SDK.16299.Desktop \
    --add Microsoft.VisualStudio.Component.VC.140 \
    --add Microsoft.VisualStudio.Component.VC.ATL \ 
    --add Microsoft.VisualStudio.Component.VC.ATLMFC \
    --add Microsoft.VisualStudio.Component.VC.CLI.Support \
  || IF "%ERRORLEVEL%"=="3010" EXIT 0
  
SHELL ["powershell.exe", "-ExecutionPolicy", "Bypass", "-Command"]

ENV chocolateyUseWindowsCompression=false

RUN iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

RUN choco install --yes cmake --params '"/InstallDir:C:\tools\cmake"'

RUN choco install --yes python3 --params '"/InstallDir:C:\tools\python3"'

RUN pip install win-unicode-console

RUN pip install \
    conan \
    conan_package_tools \
    --upgrade --force-reinstall --no-cache
 
WORKDIR "C:/Users/ContainerAdministrator"