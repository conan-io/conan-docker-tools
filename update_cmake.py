#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

if __name__ == "__main__":

    for old, new in [("3.16.1", "3.16.4"), ("v3.16", "v3.16")]:

        for root, _, filenames in os.walk("./"):
            for filename in filenames:
                if filename == "Dockerfile":
                    path = os.path.join(root, filename)
                    with open(path) as file:
                        data = file.read()

                    data = data.replace(old, new)

                    with open(path, "w") as file:
                        file.write(data)
