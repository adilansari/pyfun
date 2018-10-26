from model import Model
from models import Actor


class Movie(Model):
    id = 'id'
    imdb_id = 'imdb_id'
    title = 'title'
    director = 'director'
    year = 'year'
    rating = 'rating'
    genres = 'genres'
    runtime = 'runtime'
    country = 'country'
    language = 'language'
    imdb_score = 'imdb_score'
    imdb_votes = 'imdb_votes'
    metacritic_score = 'metacritic_score'

    @property
    def columns(self):
        return [
            self.id,
            self.imdb_id,
            self.title,
            self.director,
            self.year,
            self.rating,
            self.genres,
            self.runtime,
            self.country,
            self.language,
            self.imdb_score,
            self.imdb_votes,
            self.metacritic_score,
        ]

    @classmethod
    def table_name(cls):
        return 'movies'

    def parse_row(self, row):
        movie = Movie()
        movie.id = int(row[0])
        movie.imdb_id = row[1]
        movie.title = row[2]

        return movie

    def longest_running(self):
        query = '''SELECT * FROM {} ORDER BY {} DESC LIMIT 1'''.format(
            Movie.table_name(),
            self.runtime
        )
        return self.parse_row(self.query_db(query, one=True))

    def movie_with_most_actors(self):
        query = '''SELECT * from {} INNER JOIN
            (
                SELECT {}, COUNT({}) as movies_count from {}
                GROUP BY {}
                ORDER BY movies_count DESC
                LIMIT 1
            ) AS most_actors
            ON
            {} = most_actors.{}'''.format(
            Movie.table_name(),
            Actor.movie_id,
            Actor.id,
            Actor.table_name(),
            Actor.movie_id,
            self.id,
            Actor.movie_id
        )

        return self.parse_row(self.query_db(query, one=True))