import os
import platform
import sys

if __name__ == "__main__":
        
    for gcc_version in ["4.6", "4.8", "4.9", "5.2", "5.3", "5.4"]:
        folder_name = "gcc_%s" % gcc_version
        image_name = "lasote/conangcc%s" % gcc_version.replace(".", "")
        os.system("cd %s && ./build.sh" % folder_name)
        os.system("sudo docker push %s" % image_name)
