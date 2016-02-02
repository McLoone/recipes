import json
from flask import Flask, request, current_app
from web.recipe import RecipeStore, Recipe

app = Flask(__name__)
with app.app_context():
    current_app.recipe_store = RecipeStore()


@app.route('/recipes')
def list_recipes():
    recipes = current_app.recipe_store.list_recipes()
    return json.dumps(recipes, default=lambda obj: obj.__dict__, sort_keys=True)


@app.route('/recipes/<recipe_id>')
def lget_recipe_by_id(recipe_id):
    recipe = current_app.recipe_store.get_recipe(recipe_id)
    if recipe is None:
        return "Recipe not found", 404
    else:
        return json.dumps(recipe, default=lambda obj: obj.__dict__, sort_keys=True)


@app.route('/recipes', methods=['POST'])
def add_recipe():
    json_data = request.data.decode('utf-8')
    return current_app.recipe_store.add_recipe(Recipe.from_json(json_data))


@app.route('/recipes/<recipe_id>', methods=['DELETE'])
def remove_recipe(recipe_id):
    recipe = current_app.recipe_store.remove_recipe(recipe_id)
    if recipe is None:
        return "Recipe not found", 404
    else:
        return json.dumps(recipe, default=lambda obj: obj.__dict__, sort_keys=True)


if __name__ == "__main__":
    app.run()
