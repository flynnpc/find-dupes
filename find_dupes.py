#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os

# Constants
IMAGE_FILE_TYPES = (
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".bmp",
    ".tiff",
    ".svg",
    ".webp",
    ".heic",
    "heif",
    ".raw",
    ".nef",
)


def add_to_image_hashes(file_path, image_hashes={}):
    """
    Generate an MD5 hash for a file. and check if it's in the image hashes dictionary.
    If it is, update the list of paths for that hash. If not, add a new entry with the hash and the file path.

    Args:
    file_path (str): The path to the file.
    image_hashes (dict): A dictionary to store file hashes and their corresponding paths.

    Returns:
    dict: Updated dictionary of file hashes and their corresponding paths.
    """

    with open(file_path, "rb") as file:
        file_content = file.read()
        hasher = hashlib.md5()
        hasher.update(file_content)
        image_hash = hasher.hexdigest()

        if image_hash in image_hashes:
            image_hashes[image_hash].append(file_path)
        else:
            image_hashes[image_hash] = [file_path]

    return image_hashes


def build_image_hashes(directory, image_hashes={}):
    """
    Traverse a directory and build a dictionary of image file hashes and their corresponding paths.

    Args:
    directory (str): The path to the directory to traverse.
    image_hashes (dict): A dictionary to store file hashes and their corresponding paths.

    Returns:
    dict: Updated dictionary of file hashes and their corresponding paths.
    """

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            if os.path.isfile(file_path) and file_path.lower().endswith(
                IMAGE_FILE_TYPES
            ):
                image_hashes = add_to_image_hashes(file_path, image_hashes)

    return image_hashes


def main():
    directory_to_check = input("Enter the directory path to check for duplicates: ")

    image_hashes = build_image_hashes(directory_to_check)

    with open("image_hashes.txt", "w") as file:
        for hash_value, paths in image_hashes.items():
            if len(paths) > 1:
                file.write(f"{hash_value}:\n")
                for image_path in paths:
                    file.write(f"  {image_path}\n")
                file.write("\n")


if __name__ == "__main__":
    main()
