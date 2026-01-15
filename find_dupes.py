#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# /Users/paulflynn/Dev/test_data/source

import os
import sys

from utils.get_file_paths_in_directories import get_file_paths_in_directories
from utils.hash_helpers import build_media_hashes
from utils.organizer_helpers import rename_and_move_media_files
from utils.pruning import prune_media_paths


def main():
    directory_to_check = input(
        "Enter the directory path/s to check for duplicates. Separate by a comma: "
    ).split(",")

    files_to_process = get_file_paths_in_directories(directory_to_check)

    media_hashes = build_media_hashes(files_to_process)

    # Accepted arguments for tools ['find_dupes', 'prune_media', 'organize']
    tool_name = sys.argv[1]

    if tool_name == "find_dupes":

        with open("image_hashes.txt", "w") as hash_text:
            # for hash_value, path in image_hashes.items():
            for hash in media_hashes:
                if len(media_hashes[hash]) > 1:
                    hash_text.write(f"{hash}:\n")
                    for image_path in media_hashes[hash]:
                        hash_text.write(f"  {image_path}\n")
                    hash_text.write("\n")

    if tool_name == "prune_media":
        # ToDo - This is hard coded to a 0, but will be the input from a dropdowns of
        # directories once a GUI is implemented.

        # dir_to_keep: str = directory_to_check[0]
        # pruned_paths = prune_media_paths(media_hashes, dir_to_keep)

        pruned_paths = prune_media_paths(media_hashes)
        if not pruned_paths:
            return

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
