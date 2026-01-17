import os

from send2trash import send2trash

from utils.error_handling import (
    path_to_remove_does_not_exist,
    path_to_remove_general_error,
    path_to_remove_is_directory,
)


def prune_media_paths(
    media_hashes: dict[str, list[str]], dir_to_keep: str = ""
) -> dict[str, str]:
    """
    Move duplicate media files to trash given a dictionary of media hashes(k) and file paths to duplicates(v).

    Args:
        media_paths (dict[str, list[str]]): dictionary of media hashes(k) and a list of their duplicate file paths(v).
        dir_to_keep (str): Prefered directory path of media file to keep. Defaults to first encountered media path.

    Returns:
        dict[str, str]: A dictionary of the media hash and the remaining media file path.
    """

    pruned_paths: dict[str, str] = {}

    for hash in media_hashes:
        paths_count = len(media_hashes[hash])

        for index, path in enumerate(media_hashes[hash], start=1):

            root_path = os.path.split(path)[0]
            if dir_to_keep and dir_to_keep == root_path:
                pruned_paths[hash] = path
                continue

            if index == paths_count:
                pruned_paths[hash] = path
                continue
            try:
                # This is where to put a function that writes (a) to file keeping track of trashed files
                send2trash(path)
                continue
            except FileNotFoundError as e:
                path_to_remove_does_not_exist(path, e)
                continue
            except OSError as e:
                path_to_remove_is_directory(path, e)
                continue
            except Exception as e:
                path_to_remove_general_error(path, e)
                continue

    return pruned_paths
