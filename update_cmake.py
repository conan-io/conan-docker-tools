#!/usr/bin/env python

import os

if __name__ == "__main__":

    old = "cmake==3.15.*"
    new = "cmake==3.16.*"

    for root, _, filenames in os.walk("./"):
        for filename in filenames:
            if filename == "Dockerfile":
                path = os.path.join(root, filename)
                with open(path) as file:
                    data = file.read()

                data = data.replace(old, new)

                with open(path, "w") as file:
                    file.write(data)
