import uuid
import json

class RecipeStore:
    def __init__(self):
        self._recipes = dict()

    def add_recipe(self, recipe):
        recipe.recipe_id = uuid.uuid4().hex
        self._recipes[recipe.recipe_id] = recipe
        return recipe.recipe_id

    def remove_recipe(self, recipe_id):
        recipe_to_remove = self._recipes.get(recipe_id)
        if recipe_to_remove is not None:
            del self._recipes[recipe_id]
        return recipe_to_remove

    def list_recipes(self):
        return list(self._recipes.values())

    def get_recipe(self, recipe_id):
        return self._recipes.get(recipe_id)


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

        if recipe_id is not None:
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
        return Recipe(**json.loads(json_data, 'utf-8'))

    def to_json(self):
        return json.dumps(self, default=lambda obj: obj.__dict__, sort_keys=True, indent=4)


class Ingredient:
    def __init__(self, ingredient, amount, unit):
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit
