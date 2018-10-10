from models import model
from tests import BaseTest


class ModelTest(BaseTest):

    def test_create_filter(self):
        id_filter = model.gen_filter_param('id')
        self.assertEquals(id_filter, 'id = ?')

        filters = model.gen_filter_param('x', 'y', 'z')
        self.assertEquals(filters, 'x = ?, y = ?, z = ?')
