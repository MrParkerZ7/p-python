from time import sleep
import unittest
import os
from src.file.scan import *
from src.file.manager import *
from src.os.path import *

currentPath = get_parent_path(__file__)
file_test = f"{currentPath}\\file_test\\"
file_test_user_json = f"{file_test}User.json"


class MyTestCase(unittest.TestCase):
    def test_scan_path(self):
        newFileTest = f"{currentPath}\\test_scan_path\\"
        copy_source(file_test, newFileTest)

        listPath: Iterable[str] = []
        scan_path(newFileTest, lambda path: listPath.append(path))
        self.assertEqual(4, listPath.__len__())

        remove_auto(newFileTest)
        self.assertEqual(False, check_is_path_file(newFileTest))

    def test_scan_file(self):
        newFileTest = f"{currentPath}\\test_scan_file\\"
        copy_source(file_test, newFileTest)

        listFile: Iterable[str] = []
        scan_file(newFileTest, lambda path: listFile.append(path))
        self.assertEqual(3, listFile.__len__())

        remove_auto(newFileTest)
        self.assertEqual(False, check_is_path_file(newFileTest))

    def test_scan_dir(self):
        newFileTest = f"{currentPath}\\test_scan_dir\\"
        copy_source(file_test, newFileTest)

        listFile: Iterable[str] = []
        scan_dir(newFileTest, lambda path: listFile.append(path))
        self.assertEqual(1, listFile.__len__())

        remove_auto(newFileTest)
        self.assertEqual(False, check_is_path_file(newFileTest))

    def test_scan_remove(self):
        newFileTest = f"{currentPath}\\test_scan_remove\\"
        newFileTestPy = f"{newFileTest}Demo.py"
        copy_source(file_test, newFileTest)

        self.assertEqual(True, check_is_path_file(newFileTestPy))
        scan_remove(newFileTest, lambda path: check_file_type(path, '.py'))
        self.assertEqual(False, check_is_path_file(newFileTestPy))

        listFile: Iterable[str] = []
        scan_path(newFileTest, lambda path: listFile.append(path))
        self.assertEqual(3, listFile.__len__())

        remove_auto(newFileTest)
        self.assertEqual(False, check_is_path_file(newFileTest))
