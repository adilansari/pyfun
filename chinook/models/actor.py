from model import Model


class Actor(Model):
    id = 'id'
    movie_id = 'movie_id'
    imdb_id = 'imdb_id'
    name = 'name'

    @property
    def columns(self):
        pass

    @property
    def table_name(self):
        return 'actors'

    def parse_row(self, row):
        pass
