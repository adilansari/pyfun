class Config:
    DATABASE_URI = '/Users/reoxy/onebox/pyfun/chinook/dump/movies.db'
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    DATABASE_URI = '/Users/reoxy/onebox/pyfun/chinook/tests/dump/test.db'
    DEBUG = True
    TESTING = True

