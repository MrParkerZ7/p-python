import json
from typing import Iterable


def get_lines_of_file(filePath: str) -> Iterable[str]:
    with open(filePath, 'r', encoding='utf-8') as file:
        return file.readlines()


def write_file_from_lines(writePath: str, lines: Iterable[str]) -> list:
    with open(writePath, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def get_str_of_file(filePath: str) -> str:
    with open(filePath, 'r') as file:
        return file.read()


def get_object_from_file(filePath: str):
    return json.loads(get_str_of_file(filePath))


def get_object_from_file_byte(filePath: str) -> dict:
    with open(filePath, 'rb') as file:
        return json.load(file)
