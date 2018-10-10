class Config:
    DATABASE_URI = "dump/chinook.db"
    DEBUG = False
    TESTING = False


class TestConfig(Config):
    DEBUG = True
    TESTING = True




