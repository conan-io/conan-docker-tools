import argparse

def update_versions(file_path, new_version):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith('CONAN_VERSION='):
                file.write(f'CONAN_VERSION={new_version}\n')
            elif line.startswith('DOCKER_TAG='):
                file.write(f'DOCKER_TAG={new_version}\n')
            elif line.startswith('DOCKER_BUILD_TAG='):
                file.write(f'DOCKER_BUILD_TAG={new_version}\n')
            else:
                file.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Update Conan version to be used in the Docker image.')
    parser.add_argument('conan_version', type=str, help='The new version to set.')

    args = parser.parse_args()

    for file_path in ['legacy/.env', 'modern/.env']:
        update_versions(file_path, args.conan_version)
        print(f"Updated CONAN_VERSION and DOCKER_TAG to {args.conan_version} in {file_path}")
