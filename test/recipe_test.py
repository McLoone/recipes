import unittest
import json
from recipe import RecipeStore, Recipe


class RecipeTest(unittest.TestCase):
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
        self.recipe_store = RecipeStore()

    def test_add_recipe(self):
        recipe = Recipe.from_json(RecipeTest.RECIPE)

        recipe.recipe_id = self.recipe_store.add_recipe(recipe)

        self.assertListEqual([recipe], self.recipe_store.list_recipes())

    def test_add_multiple_recipes(self):
        recipe1 = Recipe("description1")
        recipe2 = Recipe("description2")
        recipe3 = Recipe("description3")
        recipe1.recipe_id = self.recipe_store.add_recipe(recipe1)
        recipe2.recipe_id = self.recipe_store.add_recipe(recipe2)
        recipe3.recipe_id = self.recipe_store.add_recipe(recipe3)

        return_list = self.recipe_store.list_recipes()
        return_list.sort(key=lambda r: r.description)

        self.assertListEqual([recipe1, recipe2, recipe3], return_list)

    def test_fetch_from_empty_store(self):
        self.assertListEqual([], self.recipe_store.list_recipes())

    def test_delete_recipe(self):
        recipe = Recipe.from_json(RecipeTest.RECIPE)

        recipe.recipe_id = self.recipe_store.add_recipe(recipe)
        self.assertListEqual([recipe], self.recipe_store.list_recipes())

        removed_recipe = self.recipe_store.remove_recipe(recipe.recipe_id)
        self.assertListEqual([], self.recipe_store.list_recipes())

    def test_delete_missing_recipe(self):
        removed_recipe = self.recipe_store.remove_recipe('missing')
        self.assertEquals(removed_recipe, None)

    def test_recipe_to_json(self):
        recipe = Recipe(author="Author", description="Description", time=30)
        json_recipe = recipe.to_json()
        self.assertEquals(json_recipe, RecipeTest.RECIPE)

    def test_json_to_recipe(self):
        recipe = Recipe.from_json(RecipeTest.RECIPE)
        self.assertEquals(recipe.author, "Author")
        self.assertEquals(recipe.description, "Description")
        self.assertEquals(recipe.time, 30)
        self.assertEquals(recipe.default_portions, 4)
        self.assertEquals(recipe.ingredients, [])
        self.assertEquals(recipe.steps, [])
        self.assertEquals(recipe.tags, [])

    def test_recipe_to_json_to_recipe(self):
        recipe = Recipe.from_json(RecipeTest.RECIPE)
        json_recipe = recipe.to_json()
        self.assertEquals(json_recipe, RecipeTest.RECIPE)

