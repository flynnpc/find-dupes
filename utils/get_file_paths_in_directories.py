import os

from utils.error_handling import path_is_not_file


def get_file_paths_in_directories(directories: list[str]) -> list[str]:
    file_paths_to_process = []

    for dir in directories:
        for root, _, files in os.walk(dir):
            for filename in files:
                file_path = os.path.join(root, filename)

                if os.path.isfile(file_path):
                    file_paths_to_process.append(file_path)
                else:
                    path_is_not_file(file_path)
                    continue

    return file_paths_to_process
