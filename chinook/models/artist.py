from model import Model


class Artist(Model):

    @property
    def table_name(self):
        return 'artists'

    def get_artist_count(self):
        pass

    def get_artist(self, id):
        pass

    def get_all_artists(self):
        pass

    def artists_sold_per_country(self):
        pass
