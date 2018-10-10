from abc import ABCMeta, abstractproperty


class Model(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def table_name(self):
        pass

    def query_db(self, query, args=(), one=False):
        from app import app
        cur = app.db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
