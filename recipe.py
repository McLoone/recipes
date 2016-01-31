import uuid
import json


class RecipeStore:
    def __init__(self):
        self._recipes = dict()

    def add_recipe(self, recipe):
        recipe.recipe_id = uuid.uuid4()
        self._recipes[recipe.recipe_id] = recipe
        return recipe.recipe_id

    def remove_recipe(self, recipe_id):
        recipe_to_remove = self._recipes[recipe_id]
        del self._recipes[recipe_id]
        return recipe_to_remove

    def list_recipes(self):
        return list(self._recipes.values())


class Recipe:
    def __init__(self, description,
                 recipe_id=None,
                 author="Unknown",
                 default_portions=4,
                 time=None,
                 steps=None,
                 ingredients=None,
                 tags=None):
        if steps is None:
            steps = []
        if ingredients is None:
            ingredients = []
        if tags is None:
            tags = []
        self.recipe_id = recipe_id
        self.description = description
        self.tags = tags
        self.author = author
        self.default_portions = default_portions
        self.time = time
        self.steps = steps
        self.ingredients = ingredients

    @classmethod
    def from_json(cls, json_data):
        return Recipe(recipe_id=json_data['recipe_id'],
                      description=json_data['description'],
                      author=json_data['author'],
                      default_portions=json_data['default_portions'],
                      time=json_data['time'],
                      steps=json_data['steps'],
                      ingredients=json_data['ingredients'],
                      tags=json_data['tags'])

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)


class Ingredient:
    def __init__(self, ingredient, amount, unit):
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit
