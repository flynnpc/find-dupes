import os

from send2trash import send2trash

from utils.error_handling import (
    directory_does_not_exist,
    directory_to_keep_out_of_range,
    no_directories_to_check,
    path_to_remove_does_not_exist,
    path_to_remove_general_error,
    path_to_remove_is_directory,
)
from utils.hash_helpers import build_media_hashes


def prune_media_paths(media_paths: list[set], dir_to_keep: str = "") -> list[str]:
    """
    Given a list of sets of media paths, enumerate the sets into [index, path].
    remove (delete from os) all paths with root paths that do not match the specified directory to keep.
    If no conditions are met by the index matching the length of the set (last in loop), keep the last path by default.

    Args:
        media_paths (list[set]): list of sets of media paths.
        dir_to_keep (str): Directory path of file to keep in th epruning process if encountered.

    Returns:
        list[str]: List of pruned media paths. This ordered list should match the inputed media_paths list's
        hash entries one to one.
    """

    pruned_paths: list[str] = []
    for path_set in media_paths:
        # print(list(enumerate(path_set, start=1)))
        for path in list(enumerate(path_set, start=1)):
            root_path = os.path.split(path[1])[0]
            print(f"after enumerate: {path} {root_path}")

            if dir_to_keep == root_path or path[0] == len(path):
                pruned_paths.append(path[1])
                break
            else:
                try:
                    print("path", path[1])
                    send2trash(path[1])
                    return
                except FileNotFoundError as e:
                    path_to_remove_does_not_exist(path[1], e)
                    continue
                except OSError as e:
                    path_to_remove_is_directory(path[1], e)
                    continue
                except Exception as e:
                    path_to_remove_general_error(path[1], e)
                    continue

    return pruned_paths


def prune_media_directories(
    directories_to_check: list[str], directory_to_keep_index: int = 0
) -> dict[str, str]:
    """
    Checks directories for duplicates and removes all media paths except for the one specified
    in the directory to keep. Defaults to first directory in list.

    Args:
        directories_to_check (list[str]): List of directory paths to check for duplicates.
        directory_to_keep (int): Index of the directory to keep in the list.

    Returns:
        None
    """
    if not directories_to_check:
        no_directories_to_check()
        return

    for dir_path in directories_to_check:
        if not os.path.isdir(dir_path):
            directory_does_not_exist(dir_path)
            return

    # Probably not neccessary once a GUI is implemented and drop downs are used.
    if directory_to_keep_index < 0 or directory_to_keep_index >= len(
        directories_to_check
    ):
        directory_to_keep_out_of_range(directories_to_check, directory_to_keep_index)
        return

    dir_to_keep: str = directories_to_check[directory_to_keep_index]

    media_hashes: dict = {}

    for dir_path in directories_to_check:
        media_hashes = build_media_hashes(dir_path, media_hashes)
    print("media_hashes", media_hashes.values())
    pruned_paths = prune_media_paths(media_hashes.values(), dir_to_keep)

    # ToDo - instead of writing a log file in prune_media_paths, use this return
    # to build a log file in find_dupes.py

    # This breaks at zip. Returns empty {} and needs defense
    print("zip logic", dict(zip(media_hashes.keys(), pruned_paths)))
    return dict(zip(media_hashes.keys(), pruned_paths))
