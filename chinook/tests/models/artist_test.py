from models import artist, Artist
from tests import BaseTest


class ArtistTest(BaseTest):

    def test_column_count(self):
        self.assertEquals(len(artist.columns), 2)

    def test_table_name(self):
        self.assertEquals(artist.table_name, 'artists')

    def test_get_artist_count(self):
        self.assertEquals(artist.count(), 275)

    def test_get_artist(self):
        result = artist.get_artist(22)
        self.assertIn('Led Zeppelin', result.name)
        self.assertEquals(22, result.artist_id)
