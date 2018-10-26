from model import Model


class Actor(Model):
    id = 'id'
    movie_id = 'movie_id'
    imdb_id = 'imdb_id'
    name = 'name'

    @property
    def columns(self):
        pass

    @classmethod
    def table_name(cls):
        return 'actors'

    def parse_row(self, row):
        pass


        '''
        select * 
from movies
inner join
(select movie_id, count(id) as movies_count from actors group by movie_id order by movies_count desc limit 1) as xp
on
movies.id = xp.movie_id;'''
