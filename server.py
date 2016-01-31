import json
from flask import Flask, jsonify, request
from recipe import RecipeStore, Recipe

app = Flask(__name__)
recipe_store = RecipeStore()


@app.route('/recipes')
def list_recipes():
    return jsonify(recipe_store.list_recipes())


@app.route('/recipes', methods = ['POST'])
def add_recipe():
    json_data = request.get_json(force=True)
    return recipe_store.add_recipe(Recipe.from_json(json_data))

if __name__ == "__main__":
    app.run()
