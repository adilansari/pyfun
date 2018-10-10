import os
from app import app

from tests import BaseTest


class ConfigTest(BaseTest):

    def test_testing(self):
        self.assertTrue(app.config.TESTING)

    def test_db_file(self):
        self.assertTrue(os.path.exists(app.config.DATABASE_URI))
