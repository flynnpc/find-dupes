from datetime import datetime
from io import TextIOWrapper
from subprocess import CompletedProcess


def error_log_timestamp(write_file: TextIOWrapper):
    write_file.write(f"\n{'='*20} Error Log - {datetime.now()} {'='*20}\n")


def path_to_remove_does_not_exist(file_path: str, error: FileNotFoundError):

    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write(f"FileNotFoundError: {file_path} - {error}\n")


def path_to_remove_is_directory(file_path: str, error: OSError):

    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write(f"OSError: {file_path} - {error}\n")


def path_to_remove_general_error(file_path: str, error: Exception):

    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write(f"Error: {file_path} - {error}\n")


def no_directories_to_check():
    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write("No directories provided to check.\n")


def directory_does_not_exist(dir_path: str):
    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write(f"Directory does not exist: {dir_path}\n")


def directory_to_keep_out_of_range(directories: list[str], dir_to_keep_index: int):
    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write(
            f"""Invalid directory to keep ({directories[dir_to_keep_index]}: {dir_to_keep_index})\n
                       directory to keep must be within those selected in directories list\n"""
        )


def path_is_not_file(file_path: str):
    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write(f"{file_path} is not a file.\n")


def exiftool_organize_error(dir: str, result: CompletedProcess[str]):
    with open("error_log.txt", "a") as log_file:
        error_log_timestamp(log_file)
        log_file.write(result.stdout)
        log_file.write("\n----------errors-----------\n\n")
        log_file.write(f"Errors while organizing the following directory: {dir}:\n")
        log_file.write(result.stderr)
