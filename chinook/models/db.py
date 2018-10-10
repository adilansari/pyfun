import sqlite3


class DB:
    def __init__(self, config):
        self.config = config
        self._db = None

    def get_db(self):
        if self._db is None:
            self._db = sqlite3.connect(self.config.DATABASE_URI)
        return self._db

    def close_connection(self):
        if self._db is not None:
            self._db.close()
