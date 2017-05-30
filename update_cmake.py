import os

if __name__ == "__main__":

    current_cmake_link = "https://cmake.org/files/v3.7/cmake-3.7.2-Linux-x86_64.tar.gz"
    new_cmake_link = "https://cmake.org/files/v3.8/cmake-3.8.1.tar.gz"

    current_cmake_filename = current_cmake_link.split("/")[-1]
    new_cmake_filename = new_cmake_link.split("/")[-1]

    for root, filename, _ in os.walk("./"):
        if filename == "Dockerfile":
            path = os.path.join(root, filename)
            with open(path) as file:
                data = file.read()

            data = data.replace(current_cmake_link, new_cmake_link)
            data = data.replace(current_cmake_filename, new_cmake_filename)

            with open(path, "w") as file:
                file.write(data)