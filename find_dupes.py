#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import sys

from utils.hash_helpers import build_media_hashes
from utils.organizer_helpers import rename_and_move_media_files
from utils.pruning import prune_media_directories


def main():
    directory_to_check = input(
        "Enter the directory path/s to check for duplicates. Separate by a comma: "
    ).split(",")

    # Accepted arguments for tools ['find_dupes', 'prune_media', 'organize']
    tool_name = sys.argv[1]

    if tool_name == "find_dupes":
        image_hashes = build_media_hashes(directory_to_check)

        with open("image_hashes.txt", "w") as metadata:
            for hash_value, path in image_hashes.items():
                if len(path) > 1:
                    metadata.write(f"{hash_value}:\n")
                    for image_path in path:
                        metadata.write(f"  {image_path}\n")
                    metadata.write("\n")

    if tool_name == "prune_media":
        # ToDo - This is hard coded to a 0, but will be the input from a dropdowns of
        # directories once a GUI is implemented.
        dir_to_keep_index: int = 0

        pruned_paths = prune_media_directories(directory_to_check, dir_to_keep_index)

        if pruned_paths is None:
            return
        with open("remaining_file_paths.txt", "w") as metadata:
            for hash_value, path in pruned_paths.items():
                metadata.write(f"{hash_value}: {path}\n")
                metadata.write("\n")

    if tool_name == "organize":
        cwd = os.getcwd()
        target_directory = os.path.join(cwd, "tmp")
        test_input = input(
            "Create printout of changes before actually moving files? True/False "
        )
        test = test_input == "True"

        rename_and_move_media_files(target_directory, directory_to_check, test)


if __name__ == "__main__":
    main()
