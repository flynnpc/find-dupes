import os

from utils.error_handling import path_is_not_file


def get_file_paths_in_directory(directory: str) -> list[str]:
    file_paths_to_process = []

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)

            if os.path.isfile(file_path):
                file_paths_to_process.append(file_path)
            else:
                path_is_not_file(file_path)
                continue

    return file_paths_to_process
