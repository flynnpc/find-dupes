import os

import exiftool


def walk_for_create_date_tags(directory: str):
    with exiftool.ExifToolHelper() as et:

        files_metada = []

        media_files = os.walk(directory)
        for root, _, files in media_files:
            for filename in files:
                file_path = os.path.join(root, filename)
                metadata = et.get_tags(
                    file_path,
                    tags=["CreateDate"],
                )
                for d in metadata:
                    files_metada.append(d)

        return files_metada
