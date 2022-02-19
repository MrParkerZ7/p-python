import json
from typing import Iterable


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


def remove_path(path: str):
    pass
