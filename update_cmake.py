import os

if __name__ == "__main__":

    for old, new in [("3.10.1", "3.10.1"), ("v3.10", "v3.10")]:

        for root, _, filenames in os.walk("./"):
            for filename in filenames:
                if filename == "Dockerfile":
                    path = os.path.join(root, filename)
                    with open(path) as file:
                        data = file.read()

                    data = data.replace(old, new)

                    with open(path, "w") as file:
                        file.write(data)
