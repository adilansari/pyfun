from model import Model, gen_filter_param

# - Return sold artist frequency per country.
class Artist(Model):

    artist_id = 'ArtistId'
    name = 'Name'

    @property
    def table_name(self):
        return 'artists'

    @property
    def columns(self):
        return [self.artist_id, self.name]

    def get_artist(self, id):
        return self.get_one(self.columns, gen_filter_param(Artist.artist_id), id)

    def get_all_artists(self):
        pass

    def artists_sold_per_country(self):
        pass
