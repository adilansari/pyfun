from models.db import DB
from config import Config, TestConfig


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


app = App('prod')