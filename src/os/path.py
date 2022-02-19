import os


def get_file_name(file) -> str:
    return os.path.basename(file)


def set_os_chdir_to_file_path(file) -> None:
    os.chdir(get_parent_path(file))


def get_parent_path(fileOrPath) -> str:
    return os.path.dirname(os.path.realpath(fileOrPath))
