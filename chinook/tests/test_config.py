from tests.test_app import app, AppTest


class ConfigTest(AppTest):

    def test_testing(self):
        self.assertTrue(app.config.TESTING)
