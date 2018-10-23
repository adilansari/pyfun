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
        """
        :return: :seq: - order of columns in table
        """
        return [self.artist_id, self.name]

    def parse_row(self, row):
        artist = Artist()
        artist.artist_id = int(row[0])
        artist.name = str(row[1])
        return artist

    def get_artist(self, id):
        return self.get_one(self.columns, gen_filter_param(Artist.artist_id), id)

    def get_all_artists(self):
        pass

    def artists_sold_per_country(self):
        pass
