from models import movie, Movie
from tests import BaseTest


class MovieTest(BaseTest):

    def test_table_name(self):
        self.assertEquals(Movie.table_name(), 'movies')

    def test_longest_running(self):
        self.assertEquals(movie.longest_running().title, 'Gangs of Wasseypur')

    def test_movie_with_most_actors(self):
        movie_with_most_actors = movie.movie_with_most_actors()
        self.assertEquals(movie_with_most_actors.title, 'The Dark Knight Rises')