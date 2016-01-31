import unittest
from recipe import RecipeStore, Recipe


class RecipeTest(unittest.TestCase):
    def setUp(self):
        self.recipe_store = RecipeStore()

    def test_add_recipe(self):
        recipe = Recipe("description")

        recipe.id = self.recipe_store.add_recipe(recipe)

        self.assertListEqual([recipe], self.recipe_store.list_recipes())

    def test_add_multiple_recipies(self):
        recipe1 = Recipe("description1")
        recipe2 = Recipe("description2")
        recipe3 = Recipe("description3")
        recipe1.id = self.recipe_store.add_recipe(recipe1)
        recipe2.id = self.recipe_store.add_recipe(recipe2)
        recipe3.id = self.recipe_store.add_recipe(recipe3)

        return_list = self.recipe_store.list_recipes()
        return_list.sort(key=lambda r: r.description)

        self.assertListEqual([recipe1, recipe2, recipe3], return_list)

    def test_fetch_from_empty_store(self):
        self.assertListEqual([], self.recipe_store.list_recipes())

    def test_delete_recipe(self):
        recipe = Recipe("description")

        recipe.id = self.recipe_store.add_recipe(recipe)
        self.assertListEqual([recipe], self.recipe_store.list_recipes())

        removed_recipe = self.recipe_store.remove_recipe(recipe.id)
        self.assertListEqual([], self.recipe_store.list_recipes())