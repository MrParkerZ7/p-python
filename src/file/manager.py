import os
import json
import shutil
from typing import Iterable
from distutils.dir_util import copy_tree, remove_tree, mkpath, create_tree

from ..os.path import get_parent_path


def read_file_to_lines(filePath: str) -> Iterable[str]:
    with open(filePath, 'r', encoding='utf-8') as file:
        return file.readlines()


def read_file_to_str(filePath: str) -> str:
    with open(filePath, 'r') as file:
        return file.read()


def read_file_to_object(filePath: str) -> dict:
    return json.loads(read_file_to_str(filePath))


def read_file_byte_to_object(filePath: str) -> dict:
    with open(filePath, 'rb') as file:
        return json.load(file)


def write_file_from_lines(writePath: str, lines: Iterable[str], auto_create_tree_path: bool = True) -> list:
    if(auto_create_tree_path):
        create_tree_parent_path(writePath)
    with open(writePath, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def write_file_from_str(writePath: str, str: str, auto_create_tree_path: bool = True) -> list:
    if(auto_create_tree_path):
        create_tree_parent_path(writePath)
    with open(writePath, 'w', encoding='utf-8') as file:
        file.write(str)


def check_path_existing(path: str):
    return os.path.exists(path)


def check_is_path_file(path: str):
    return os.path.isfile(path)


def check_is_path_dir(path: str):
    return os.path.isdir(path)


def check_file_type(path: str, fileType: str):  # make dynamic fileType and path
    if not fileType.startswith('.'):
        fileType = '.'+fileType
    return check_is_path_file(path) and path.endswith(fileType)


def copy_source(sourcePath: str, toPath):
    copy_tree(sourcePath, toPath)


def create_dir(path: str, exist_ok: bool = True):
    os.makedirs(path, exist_ok=exist_ok)


def create_tree_parent_path(writePath):
    parentPath = get_parent_path(writePath)
    if not check_is_path_file(parentPath):
        create_dir(parentPath)


def remove_path(path: str):
    shutil.rmtree(path)


def remove_file(path: str):
    os.remove(path)


def remove_auto(path: str, non_exist_ok: bool = True):
    if check_path_existing(path) or not non_exist_ok:
        if os.path.isfile(path):
            remove_file(path)
        else:
            remove_path(path)
