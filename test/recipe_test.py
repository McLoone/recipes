import unittest
from recipe import RecipeStore, Recipe


class RecipeTest(unittest.TestCase):
    def test_add_recipe(self):
        recipeStore = RecipeStore()
        recipe = Recipe("description")

        recipeStore.add_recipe(recipe)

        self.assertListEqual([recipe], recipeStore.recipes)

    def test_add_multiple_recipies(self):
        recipeStore = RecipeStore()
        recipe1 = Recipe("description1")
        recipe2 = Recipe("description2")
        recipe3 = Recipe("description3")

        recipeStore.add_recipe(recipe1)
        recipeStore.add_recipe(recipe2)
        recipeStore.add_recipe(recipe3)

        self.assertListEqual([recipe1, recipe2, recipe3], recipeStore.recipes)

