from time import sleep
import unittest
import os
from src.file.manager import *
from src.os.path import *

currentPath = get_parent_path(__file__)
file_test = f"{currentPath}\\file_test\\"
file_test_user_json = f"{file_test}User.json"


class MyTestCase(unittest.TestCase):

    def test_list_str_from_file(self):
        self.assertEqual(
            ['{\n', '   "name": "Puck",\n', '   "age": 99\n', '}'],
            read_file_to_lines(file_test_user_json))

    def test_read_file_to_str(self):
        self.assertEqual(
            '{\n   "name": "Puck",\n   "age": 99\n}',
            read_file_to_str(file_test_user_json))

    def test_read_file_to_object(self):
        self.assertEqual(
            {'name': 'Puck', 'age': 99},
            read_file_to_object(file_test_user_json))

    def test_read_file_byte_to_object(self):
        self.assertEqual(
            {'name': 'Puck', 'age': 99},
            read_file_byte_to_object(file_test_user_json))

    def test_check_path_existing(self):
        self.assertEqual(
            True,
            check_path_existing(file_test))
        self.assertEqual(
            False,
            check_path_existing(file_test + '_non'))

        self.assertEqual(
            True,
            check_path_existing(file_test_user_json))
        self.assertEqual(
            False,
            check_path_existing(f'{file_test_user_json}.py'))

    def test_check_file_existing(self):
        self.assertEqual(
            False,
            check_file_existing(file_test))
        self.assertEqual(
            True,
            check_file_existing(file_test_user_json))
        self.assertEqual(
            False,
            check_file_existing(f'{file_test_user_json}.py'))

    def test_check_file_type(self):
        self.assertEqual(
            True,
            check_file_type(file_test_user_json, '.json'))
        self.assertEqual(
            True,
            check_file_type(file_test_user_json, 'json'))
        self.assertEqual(
            False,
            check_file_type(file_test_user_json+'.py', 'json'))
        self.assertEqual(
            False,
            check_file_type(currentPath, 'json'))

    def test_write_file_from_lines(self):
        newInfo = f"{file_test}new_info.text"
        if(check_path_existing(newInfo)):
            remove_auto(newInfo)
            sleep(1)
        self.assertEqual(
            None,
            write_file_from_lines(
                newInfo,
                ['info\n', 'info\n', 'info\n']))
        self.assertEqual(True, check_path_existing(newInfo))
        remove_auto(newInfo)

    def test_write_file_from_str(self):
        newInfo = f"{file_test}new_info.text"
        if(check_path_existing(newInfo)):
            remove_auto(newInfo)
            sleep(1)
        self.assertEqual(
            None,
            write_file_from_str(
                newInfo,
                'info\ninfo\ninfo\n'))
        self.assertEqual(True, check_path_existing(newInfo))
        remove_auto(newInfo)

    def test_write_file_from_str_in_deeper_path(self):
        deepPath = f"{file_test}deeper_path"
        newInfo = f"{deepPath}\\new_info.text"
        if(check_path_existing(newInfo)):
            remove_auto(newInfo)
            sleep(1)
        self.assertEqual(
            None,
            write_file_from_str(
                newInfo,
                'info\ninfo\ninfo\n'))
        self.assertEqual(True, check_path_existing(newInfo))
        remove_auto(newInfo)
        self.assertEqual(True, check_path_existing(deepPath))
        remove_auto(f"{file_test}deeper_path")
        self.assertEqual(False, check_path_existing(deepPath))

    def test_remove_file_auto(self):
        testBuild = f"{file_test}build"
        remove_auto(testBuild)
        create_dir(testBuild, True)
        with self.assertRaises(FileExistsError):
            create_dir(testBuild, False)

        remove_auto(testBuild)
        self.assertEqual(False, check_path_existing(testBuild))

    def test_copy_source(self):
        newFileTest = f"{currentPath}\\new_file_test\\"
        newFileTestUser = f"{newFileTest}User.json"
        newFileTestDemo = f"{newFileTest}Demo.py"
        copy_source(file_test, newFileTest)
        self.assertEqual(True, check_file_existing(newFileTestUser))
        self.assertEqual(True, check_file_existing(newFileTestDemo))
        remove_auto(newFileTest)
        self.assertEqual(False, check_file_existing(newFileTestUser))
        self.assertEqual(False, check_file_existing(newFileTestDemo))
