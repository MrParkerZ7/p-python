import unittest
import os
from src.file.manager import *
from src.os.path import *

currentPath = get_parent_path(__file__)


class MyTestCase(unittest.TestCase):
    def test_list_str_from_file(self):
        self.assertEqual(
            ['{\n', '   "name": "Puck",\n', '   "age": 99\n', '}'],
            read_file_to_lines(f"{currentPath}\\file_test\\User.json")
        )
