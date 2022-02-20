import os
from .manager import *


def scan_path(path: str, arrow, logger=print) -> None:
    logger('scaning path =', path)
    listDir = os.listdir(path)
    for dir in listDir:
        logger('scaning sub path =', path)
        subPath = f"{path}\\{dir}"
        arrow(subPath)
        if os.path.isdir(subPath):
            scan_path(subPath, arrow, logger=logger)


def scan_file(path: str, arrow, logger=print) -> None:
    def check_path_is_file(path):
        if check_is_path_file(path):
            arrow(path)
    scan_path(path, check_path_is_file, logger)


def scan_dir(path: str, arrow, logger=print) -> None:
    def check_path_is_dir(path):
        if check_is_path_dir(path):
            arrow(path)
    scan_path(path, check_path_is_dir, logger)


def scan_remove(
        path: str,
        arrowReturnBool,
        non_exist_ok: bool = True,
        logger=print) -> None:

    def check_then_remove(path):
        if arrowReturnBool(path):
            remove_auto(path, non_exist_ok)

    scan_path(path, check_then_remove, logger)
