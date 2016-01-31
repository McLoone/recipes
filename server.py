import json
from flask import Flask
from recipe import RecipeStore

app = Flask(__name__)
recipe_store = RecipeStore()

@app.route("/recipes")
def list_recipes():
    return json.dumps(recipe_store.list_recipes())

if __name__ == "__main__":
    app.run()