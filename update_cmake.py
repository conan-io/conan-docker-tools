import os

if __name__ == "__main__":

    current_cmake_link = "3.8.1"
    new_cmake_link = "3.8.1"

    for root, _, filenames in os.walk("./"):
        for filename in filenames:
            if filename == "Dockerfile":
                path = os.path.join(root, filename)
                with open(path) as file:
                    data = file.read()

                data = data.replace(current_cmake_link, new_cmake_link)

                with open(path, "w") as file:
                    file.write(data)
