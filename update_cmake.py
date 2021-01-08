#!/usr/bin/env python
import os

if __name__ == "__main__":

    for old, new in [
        ("CMAKE_VERSION_MAJOR_MINOR=3.17", "CMAKE_VERSION_MAJOR_MINOR=3.18"),
        ("CMAKE_VERSION_FULL=3.18.4", "CMAKE_VERSION_FULL=3.18.5"),
    ]:

        for root, _, filenames in os.walk("./"):
            for filename in filenames:
                if filename == "Dockerfile":
                    path = os.path.join(root, filename)
                    with open(path) as file:
                        data = file.read()

                    data = data.replace(old, new)

                    with open(path, "w") as file:
                        file.write(data)
