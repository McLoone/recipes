import unittest
import server


class ServerTestCase(unittest.TestCase):

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def test_get_all_recipes_with_empty_store(self):
        result = self.app.get('/recipes')
        self.assertEquals(result.data.decode('utf-8'), "[]")
