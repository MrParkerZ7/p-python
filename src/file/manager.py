from importlib.resources import path
import json
import shutil
from typing import Iterable
import os


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


def write_file_from_lines(writePath: str, lines: Iterable[str]) -> list:
    with open(writePath, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def check_path_existing(path: str):
    return os.path.exists(path)


def check_file_type(path: str, fileType: str):
    pass


def remove_path(path: str):
    shutil.rmtree(path)


def remove_file(path: str):
    os.remove(path)


def remove_auto(path: str):
    if os.path.isfile(path):
        remove_file(path)
    else:
        remove_path(path)
