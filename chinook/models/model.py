from app import app


class Model(object):
    def __init__(self):
        pass

    def query_db(self, query, args=(), one=False):
        cur = app.db.get_db().execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv
