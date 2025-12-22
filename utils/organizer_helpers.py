import os

import exiftool

from utils.error_handling import exiftool_read_error, metadata_read_file_is_not_file

exiftool_params = [
    "-Createate",  # Tag to search for in metadata
    "-w",  # Date format to output
    "%Y-%m-%d_%H:%M:%S",  # Desired date format
]


def walk_and_create_date_tags(directory: str) -> list[dict[str, str]]:
    with exiftool.ExifToolHelper() as et:

        files_metada = []

        media_files = os.walk(directory)
        for root, _, files in media_files:
            for filename in files:
                file_path = os.path.join(root, filename)
                if not os.path.isfile(file_path):
                    metadata_read_file_is_not_file(file_path)
                    continue
                try:
                    metadata = et.execute_json(
                        *[
                            f"{file_path}",
                            *exiftool_params,
                        ]
                    )
                    for tags in metadata:
                        files_metada.append(tags)

                except Exception as e:
                    exiftool_read_error(file_path, e)
                    continue

        return files_metada
