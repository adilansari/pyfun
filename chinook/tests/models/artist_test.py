from models import artist
from tests import BaseTest


class ArtistTest(BaseTest):

    def test_table_name(self):
        self.assertEquals(artist.table_name, 'artists')

    def test_get_artist_count(self):
        self.assertEquals(artist.count(), 275)

    def test_get_artist(self):
        self.assertIn('Led Zeppelin', artist.get_artist(22))
