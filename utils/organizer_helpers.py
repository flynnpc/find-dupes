import os
from pprint import pprint

import exiftool

from utils.error_handling import exiftool_read_error, metadata_read_file_is_not_file

exiftool_tags = ["CreateDate", "DateTimeOriginal"]
# -G1 groups tags by their Groups, i.e. QuickTime, EXIF, etc.
# -a allows duplicate tags to be extracted
exiftool_params = [
    "-d %Y-%m-%d_%H:%M:%S",
    "-G1",
    "-a",
]


def walk_and_create_date_tags(directory: str) -> list[dict[str, str]]:
    with exiftool.ExifToolHelper() as et:

        files_metadata = []

        media_files = os.walk(directory)
        file_paths_to_process = []

        for root, _, files in media_files:
            for filename in files:
                file_path = os.path.join(root, filename)

                if os.path.isfile(file_path):
                    file_paths_to_process.append(file_path)
                else:
                    metadata_read_file_is_not_file(file_path)
                    continue

        # Split into two functions - get_files_tags()
        try:
            all_files_metadata = et.get_tags(
                file_paths_to_process, exiftool_tags, exiftool_params
            )

            pprint(all_files_metadata)

            for file_metadata in all_files_metadata:
                files_metadata.append(file_metadata)

        except Exception as e:
            exiftool_read_error(file_path, e)

        return files_metadata
