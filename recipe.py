class RecipeStore:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def repices(self):
        self.recipes


class Recipe:
    def __init__(self, description, time = None, steps = None, ingredients = None, author = "Unknown", default_portions = 4, tags=None):
        if tags is None:
            tags = []
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