from models import artist
from tests import BaseTest


class ArtistTest(BaseTest):

    def test_table_name(self):
        self.assertEquals(artist.table_name, 'artists')

    def test_get_artist_count(self):
        pass
