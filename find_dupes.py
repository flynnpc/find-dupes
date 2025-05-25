#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os
import shutil
import zipfile


def move_file(source, destination):
    """
    Moves a file from the source path to the destination path.

    Args:
    source (str): The path to the source file.
    destination (str): The path to the destination,
    can be a directory or a new file path.
    """
    try:
        shutil.move(source, destination)
        print(f"File '{source}' moved successfully to '{destination}'.")
    except FileNotFoundError:
        print(f"Error: File '{source}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def hash_files(directory):
    file_hashes = {}

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        with open(file_path, "rb") as file:
            file_content = file.read()
            file_hash = hashlib.md5(file_content).hexdigest()

    file_hashes[file_hash] = file_path

    return file_hashes


def find_unique_file_paths(source_hashes, directory_to_check_hashes):
    """
    Find unique file paths between two directories based on their hashes.

    Args:
    source_hashes (dict): A dictionary of file hashes from the source directory.
    directory_to_check_hashes (dict): A dictionary of file hashes from the directory to check.

    Returns:
    list: A list of paths of unique files.
    """
    unique_files = []

    for hash_value, file_path in directory_to_check_hashes.items():
        if hash_value in source_hashes:
            unique_files.append(file_path)

    return unique_files


def are_there_zips(directory):
    """
    Check if there are any zip files in the given directory.

    Args:
    directory (str): The path to the directory to check.

    Returns:
    bool: True if there are zip files, False otherwise.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            return True
    return False


def extract_zip_files(directory):
    """
    Extract all zip files in the given directory.

    Args:
    directory (str): The path to the directory containing zip files.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".zip"):
            file_path = os.path.join(directory, filename)
            with zipfile.ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(directory)


def main():
    source_directory = input("Enter the source directory path: ")
    directory_to_check = input("Enter the directory path to check for duplicates: ")

    current_directory = os.path.dirname(os.path.realpath(__file__))

    # Create a directory to store unique files
    os.makedirs(os.path.join(current_directory, "unique_files"), exist_ok=True)

    source_hashes = []
    if are_there_zips(source_directory):
        extract_zip_files(source_directory)
        source_hashes = hash_files(source_directory)
    else:
        source_hashes = hash_files(source_directory)

    directory_to_check_hashes = []
    if are_there_zips(directory_to_check):
        extract_zip_files(directory_to_check)
        directory_to_check_hashes = hash_files(directory_to_check)
    else:
        directory_to_check_hashes = hash_files(directory_to_check)

    unique_file_paths = find_unique_file_paths(source_hashes, directory_to_check_hashes)

    if unique_file_paths:
        for file_path in unique_file_paths:
            move_file(file_path, os.path.join(current_directory, "unique_files"))


if __name__ == "__main__":
    main()
