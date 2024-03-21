script_folder="/home/conan/project"
echo "echo Restoring environment" > "$script_folder/deactivate_conanrunenv-release-x86_64.sh"
for v in PATH LD_LIBRARY_PATH DYLD_LIBRARY_PATH
do
    is_defined="true"
    value=$(printenv $v) || is_defined="" || true
    if [ -n "$value" ] || [ -n "$is_defined" ]
    then
        echo export "$v='$value'" >> "$script_folder/deactivate_conanrunenv-release-x86_64.sh"
    else
        echo unset $v >> "$script_folder/deactivate_conanrunenv-release-x86_64.sh"
    fi
done


export PATH="/tmp/conan/full_deploy/host/binutils/2.41/Release/x86_64/bin:/tmp/conan/full_deploy/host/binutils/2.41/Release/x86_64/bin/exec_prefix/x86_64-pc-linux-gnu/bin:$PATH"
export LD_LIBRARY_PATH="/tmp/conan/full_deploy/host/binutils/2.41/Release/x86_64/lib:$LD_LIBRARY_PATH"
export DYLD_LIBRARY_PATH="/tmp/conan/full_deploy/host/binutils/2.41/Release/x86_64/lib:$DYLD_LIBRARY_PATH"