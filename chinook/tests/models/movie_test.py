from models import movie
from tests import BaseTest


class MovieTest(BaseTest):

    def test_table_name(self):
        self.assertEquals(movie.table_name, 'movies')

    def test_longest_running(self):
        self.assertEquals(movie.longest_running().title, 'Gangs of Wasseypur')
