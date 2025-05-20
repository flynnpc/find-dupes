#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil
import os
import os
import hashlib

def main():
    # Your code here
    pass

if __name__ == "__main__":
    main()


def move_file(source, destination):
    """
    Moves a file from the source path to the destination path.

    Args:
    source (str): The path to the source file.
    destination (str): The path to the destination, can be a directory or a new file path.
    """
    try:
        shutil.move(source, destination)
        print(f"File '{source}' moved successfully to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    # Example usage:
    source_file = "path/to/your/source/file.txt"
    destination_path = "path/to/your/destination/directory/"
    # or "path/to/new/file/path.txt" to rename while moving

    move_file(source_file, destination_path)




def find_duplicates(directory):
    file_hashes = {}
    duplicates = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        with open(file_path, 'rb') as file:
            file_content = file.read()
            file_hash = hashlib.md5(file_content).hexdigest()

    if file_hash in file_hashes:
        duplicates.append((file_hashes[file_hash], file_path))
    else:
        file_hashes[file_hash] = file_path
        return duplicates

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check for duplicates: ")

if os.path.isdir(directory_to_check):
    duplicate_files = find_duplicates(directory_to_check)

if duplicate_files:
    print("Duplicate files found:")
for file1, file2 in duplicate_files:
    print(f" - {file1} and {file2}")
#     else:
#         print("No duplicate files found in the directory.")
# else:
#     print("Invalid directory path.")