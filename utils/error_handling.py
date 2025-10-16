def path_to_remove_does_not_exist(file_path: str, error: FileNotFoundError):
    print(f"Could not delete file {file_path}: {error}")

    with open("error_log.txt", "a") as log_file:
        log_file.write(f"FileNotFoundError: {file_path} - {error}\n")


def path_to_remove_is_directory(file_path: str, error: OSError):
    print(f"Could not delete path {file_path} because it is a directory: {error}")

    with open("error_log.txt", "a") as log_file:
        log_file.write(f"OSError: {file_path} - {error}\n")


def path_to_remove_general_error(file_path: str, error: Exception):
    print(f"Could not delete path {file_path}: {error}")

    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Error: {file_path} - {error}\n")


def no_directories_to_check(directories: list[str]):
    print("No directories provided to check.")
    with open("error_log.txt", "a") as log_file:
        log_file.write("No directories provided to check.\n")


def directory_does_not_exist(dir_path: str):
    print(f"Directory does not exist: {dir_path}")
    with open("error_log.txt", "a") as log_file:
        log_file.write(f"Directory does not exist: {dir_path}\n")


def directory_to_keep_out_of_range(directories: list[str], dir_to_keep_index: int):
    print("Invalid index for directory to keep.")
    with open("error_log.txt", "a") as log_file:
        log_file.write(
            f"""Invalid directory to keep ({directories[dir_to_keep_index]}: {dir_to_keep_index})\n
                       directory to keep must be within those selected in directories list\n"""
        )
