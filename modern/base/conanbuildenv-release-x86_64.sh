script_folder="/home/conan/project"
echo "echo Restoring environment" > "$script_folder/deactivate_conanbuildenv-release-x86_64.sh"
for v in PATH GPROFNG_SYSCONFDIR
do
    is_defined="true"
    value=$(printenv $v) || is_defined="" || true
    if [ -n "$value" ] || [ -n "$is_defined" ]
    then
        echo export "$v='$value'" >> "$script_folder/deactivate_conanbuildenv-release-x86_64.sh"
    else
        echo unset $v >> "$script_folder/deactivate_conanbuildenv-release-x86_64.sh"
    fi
done


export PATH="$PATH:/tmp/conan/full_deploy/host/binutils/2.41/Release/x86_64/bin:/tmp/conan/full_deploy/host/binutils/2.41/Release/x86_64/bin/exec_prefix/x86_64-pc-linux-gnu/bin"
export GPROFNG_SYSCONFDIR="/home/conan/.conan2/p/binut373e3cbd6b532/p/etc"