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
            read_file_to_lines(file_test_user_json)
        )

    def test_read_file_to_str(self):
        self.assertEqual(
            '{\n   "name": "Puck",\n   "age": 99\n}',
            read_file_to_str(file_test_user_json)
        )

    def test_read_file_to_object(self):
        self.assertEqual(
            {'name': 'Puck', 'age': 99},
            read_file_to_object(file_test_user_json)
        )

    def test_read_file_byte_to_object(self):
        self.assertEqual(
            {'name': 'Puck', 'age': 99},
            read_file_byte_to_object(file_test_user_json)
        )

    def test_write_file_from_lines(self):
        newInfo = f"{file_test}new_info.text"
        if(check_path_existing(newInfo)):
            remove_file(newInfo)
            sleep(1)
        self.assertEqual(
            None,
            write_file_from_lines(
                newInfo,
                ['info\n', 'info\n', 'info\n'])
        )
        self.assertEqual(True, check_path_existing(newInfo))
        remove_file(newInfo)
