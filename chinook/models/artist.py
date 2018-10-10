from model import Model, gen_filter_param


class Artist(Model):

    artist_id = 'ArtistId'
    name = 'Name'

    @property
    def table_name(self):
        return 'artists'

    @property
    def get_all_columns(self):
        return [self.artist_id, self.name]

    def get_artist(self, id):
        return self.get_one(self.get_all_columns, gen_filter_param(Artist.artist_id), id)

    def get_all_artists(self):
        pass

    def artists_sold_per_country(self):
        pass
