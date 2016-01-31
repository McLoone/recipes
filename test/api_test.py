import unittest
import server
import json


class ServerTestCase(unittest.TestCase):
    RECIPE = """{
    "author": "Author",
    "default_portions": 4,
    "description": "Description",
    "ingredients": [],
    "recipe_id": null,
    "steps": [],
    "tags": [],
    "time": 30
}"""

    def setUp(self):
        server.app.config['TESTING'] = True
        self.app = server.app.test_client()

    def test_get_all_recipes_with_empty_store(self):
        response = self.app.get('/recipes')
        self.assertEquals(response.data.decode('utf-8'), "{}")

