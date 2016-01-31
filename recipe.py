import uuid


class RecipeStore:
    def __init__(self):
        self._recipes = dict()

    def add_recipe(self, recipe):
        recipe.id = uuid.uuid4()
        self._recipes[recipe.id] = recipe
        return recipe.id

    def remove_recipe(self, id):
        recipe_to_remove = self._recipes[id]
        del self._recipes[id]
        return recipe_to_remove

    def list_recipes(self):
        return list(self._recipes.values())


class Recipe:
    def __init__(self, description, author = "Unknown", default_portions = 4, time = None, steps=None, ingredients=None, tags=None):
        if steps is None:
            steps = []
        if ingredients is None:
            ingredients = []
        if tags is None:
            tags = []
        self.id = None
        self.description = description
        self.tags = tags
        self.author = author
        self.default_portions = default_portions
        self.time = time
        self.steps = steps
        self.ingredients = ingredients


class Ingredient:
    def __init__(self, ingredient, amount, unit):
        self.ingredient = ingredient
        self.amount = amount
        self.unit = unit