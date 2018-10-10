import unittest
import os
from shutil import copyfile
from app import App

app = App('test')
DB_FILE = '/Users/reoxy/onebox/pyfun/chinook/dump/chinook.db'
TEST_DB_FILE = '/Users/reoxy/onebox/pyfun/chinook/tests/dump/test.db'


class AppTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(os.path.exists(DB_FILE))
        copyfile(DB_FILE, TEST_DB_FILE)
        self.assertTrue(os.path.exists(TEST_DB_FILE))

    def tearDown(self):
        self.assertTrue(os.path.exists(TEST_DB_FILE))
        os.remove(TEST_DB_FILE)
        self.assertFalse(os.path.exists(TEST_DB_FILE))
