import os
from .manager import *


def scan_path(path: str, arrow: function(str), logger: function(object) = print) -> None:
    logger(path)
    listDir = os.listdir(path)
    for dir in listDir:
        logger(path)
        subPath = f"{path}/{dir}"
        arrow(subPath)
        if os.path.isdir(subPath):
            scan_path(subPath, arrow, logger=logger)


def scan_file(path: str, arrow: function(str), logger: function(object) = print) -> None:
    def check_then_remove(path):
        if arrow(path):
            remove_auto(path)

    scan_path(path, check_then_remove, logger)


def scan_remove(
        path: str,
        arrowReturnBool: function(str),
        non_exist_ok: bool = True,
        logger: function(object) = print) -> None:

    def check_then_remove(path):
        if arrowReturnBool(path):
            remove_auto(path, non_exist_ok)

    scan_path(path, check_then_remove, logger)
