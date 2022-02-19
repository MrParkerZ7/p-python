import os


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
    pass
