import os

if __name__ == "__main__":

    for old, new in [("3.11.2", "3.12.1"), ("v3.11", "v3.12")]:

        for root, _, filenames in os.walk("./"):
            for filename in filenames:
                if filename == "Dockerfile":
                    path = os.path.join(root, filename)
                    with open(path) as file:
                        data = file.read()

                    data = data.replace(old, new)

                    with open(path, "w") as file:
                        file.write(data)
