import os


def get_source_name_by_path(path) -> str:
    return os.path.basename(path)


def get_parent_path(fileOrPath) -> str:
    return os.path.dirname(os.path.realpath(fileOrPath))


def set_os_chdir_to_file(file) -> None:
    os.chdir(get_parent_path(file))

def set_os_chdir_path(path) -> None:
    os.chdir(path)
