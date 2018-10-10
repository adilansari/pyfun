import os
import unittest
from shutil import copyfile

DB_FILE = '/Users/reoxy/onebox/pyfun/chinook/dump/chinook.db'
TEST_DB_FILE = '/Users/reoxy/onebox/pyfun/chinook/tests/dump/test.db'


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.assertTrue(os.path.exists(DB_FILE))
        copyfile(DB_FILE, TEST_DB_FILE)
        self.assertTrue(os.path.exists(TEST_DB_FILE))

    def tearDown(self):
        os.remove(TEST_DB_FILE)
        self.assertFalse(os.path.exists(TEST_DB_FILE))
