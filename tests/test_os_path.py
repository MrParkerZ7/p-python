import unittest
import os
from src.os.path import *

currentPath = os.path.dirname(os.path.realpath(__file__))


class MyTestCase(unittest.TestCase):
    def test_get_parent_path(self):
        self.assertEqual(currentPath, get_parent_path(__file__))

    def test_get_file_name(self):
        self.assertEqual(os.path.basename(__file__), get_file_name(__file__))

    def test_set_os_chdir_to_file_path(self):
        self.assertEqual(
            get_parent_path(get_parent_path(__file__)),
            os.getcwd())

        self.assertEqual(
            None,
            set_os_chdir_to_file(get_parent_path(get_parent_path(__file__))))

        self.assertEqual(
            get_parent_path(get_parent_path(get_parent_path(__file__))),
            os.getcwd())

        set_os_chdir_path(currentPath)
        self.assertEqual(
            currentPath,
            os.getcwd())
