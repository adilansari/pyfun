from abc import ABCMeta, abstractproperty, abstractmethod
from app import app


class Model(object):
    __metaclass__ = ABCMeta

    @classmethod
    def table_name(cls):
        raise NotImplementedError('Table name is needed')

    @abstractproperty
    def columns(self):
        pass

    @abstractmethod
    def parse_row(self, row):
        pass

    def query_db(self, query, args=(), one=False):
        cur = app.db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    def get_one(self, cols_to_get, columns_filter, args):
        cols = ', '.join(cols_to_get)
        args = [args] if not type(args) == list else args
        query = '''SELECT {} FROM {} WHERE {}'''.format(cols, self.table_name(), columns_filter)
        return self.query_db(query, args, True)

    def get_many(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def count(self):
        query = '''SELECT COUNT(*) FROM {}'''.format(self.table_name())
        return int(self.query_db(query, one=True)[0])


def gen_filter_param(*column_names):
    new_vars = map(lambda x: x + ' = ?', column_names)
    return ', '.join(new_vars)
