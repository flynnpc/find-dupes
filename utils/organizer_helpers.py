import os
import subprocess

from utils.error_handling import exiftool_organize_error

testing_source = "/Users/paulflynn/Dev/test_data/source"
testing_target = "/test/"

EXIFTOOL_TEST_CMD = "-testname<"
EXIFTOOL_DIRECTORY_CMD = "-filename<"

EXIFTOOL_TAGS = ["quicktime:createdate", "exif:datetimeoriginal"]

EXIFTOOL_DATE_FILENAME_FMT = "%Y-%m-%d_%H:%M:%S%%c.%%e"


EXIFTOOL_PARAMS = [
    "-r",  # Recursive
    "-d",  # Use date format
]


def rename_and_move_media_files(
    target_path: str, file_paths_to_process: list[str], test=False
):
    """
    needs description

    Args:
        target_path (str:):
        file_paths_to_process list(str):

    Returns:
        None
    """
    params = " ".join(EXIFTOOL_PARAMS)

    output_path = os.path.join(target_path, f"%Y/{EXIFTOOL_DATE_FILENAME_FMT}")

    if test:
        tag_command: str = " ".join(
            map(
                lambda tag: f"{EXIFTOOL_TEST_CMD}{tag}",
                EXIFTOOL_TAGS,
            )
        )

    else:
        tag_command: str = " ".join(
            map(
                lambda tag: f"{EXIFTOOL_DIRECTORY_CMD}{tag}",
                EXIFTOOL_TAGS,
            )
        )

    for dir in file_paths_to_process:
        exiftool_organize_command: str = (
            f"exiftool {params} {output_path} {tag_command} {dir}"
        )

        exiftool_result = subprocess.run(
            exiftool_organize_command.split(" "), capture_output=True, text=True
        )

        if exiftool_result.stderr:
            exiftool_organize_error(dir, exiftool_result)
