import os

import exiftool


def walk_and_create_date_tags(directory: str) -> list[dict[str, str]]:
    with exiftool.ExifToolHelper() as et:

        files_metada = []

        media_files = os.walk(directory)
        for root, _, files in media_files:
            for filename in files:
                file_path = os.path.join(root, filename)
                metadata = et.execute_json(
                    *[
                        "-CreateDate",
                        "-d",
                        "%Y-%m-%d_%H:%M:%S",
                        f"{file_path}",
                    ]
                )
                for tags in metadata:
                    files_metada.append(tags)

        return files_metada
