import hashlib
import os

from constants import MEDIA_FILE_TYPES


def add_to_media_hashes(
    file_path: str, image_hashes: dict[str, set[str]] = {}
) -> dict[str, set[str]]:
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
            image_hashes[image_hash].add(file_path)
        else:
            image_hashes[image_hash] = set([file_path])

    return image_hashes


def build_media_hashes(
    directory, image_hashes: dict[str, set[str]] = {}
) -> dict[str, set[str]]:
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
                MEDIA_FILE_TYPES
            ):
                image_hashes = add_to_media_hashes(file_path, image_hashes)

    return image_hashes
