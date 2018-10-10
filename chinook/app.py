from config import Config, TestConfig
from db import DB


class App(object):
    def __init__(self, env='test'):
        self.config = self.get_config(env)
        self.db = DB(self.config)

    @classmethod
    def get_config(cls, env):
        if env == 'test':
            return TestConfig
        else:
            return Config


import os

env = os.environ.get('app_env')
app = App(env)
