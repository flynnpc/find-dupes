#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from utils.hash_helpers import build_media_hashes


def main():
    directory_to_check = input("Enter the directory path to check for duplicates: ")

    image_hashes = build_media_hashes(directory_to_check)

    with open("image_hashes.txt", "w") as file:
        for hash_value, paths in image_hashes.items():
            if len(paths) > 1:
                file.write(f"{hash_value}:\n")
                for image_path in paths:
                    file.write(f"  {image_path}\n")
                file.write("\n")


if __name__ == "__main__":
    main()
