import unittest
import server
import json


class ServerTestCase(unittest.TestCase):
    RECIPE = """{
    "author": "Author",
    "default_portions": 4,
    "description": "Description",
    "ingredients": [],
    "steps": [],
    "tags": [],
    "time": 30
}"""

    def setUp(self):
        server.app.testing = True
        self.app = server.app.test_client()

    def test_get_all_recipes_with_empty_store(self):
        response = self.app.get('/recipes')
        self.assertEquals(response.data.decode('utf-8'), "[]")

    def test_add_fetch_delete_recipe(self):
        recipe_id = self.app.post('/recipes',
                      headers={'Content-Type': 'application/json'},
                      data=ServerTestCase.RECIPE).data.decode('utf-8')
        recipes = json.loads(self.app.get('/recipes').data.decode('utf-8'))
        self.assertEquals(recipes[0]['recipe_id'], recipe_id)
        self.app.delete('/recipes/' + recipe_id)

