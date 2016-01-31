Recipes is a very small recipe backend.

Story: A User add a Recipe

As a user 
I want to add a Recipe to the RecipeStore
So I can fetch it when I want to cook some dinner

Scenario: Add recipe to RecipeStore
Given the RecipeStore is empty
When a User add a Recipe
Then the Recipe is added to the RecipeStore


Story: A User retrieves Recipes from RecipeStore

As a user
I want to fetch all available Recipes from the RecipeStore
So I can choose a meal to cook

Scenario 1: Fetch all recipes from empty RecipeStore
Given the RecipeStore is empty
When a User fetches all Recipes from the RecipeStore
Then no Recipes are returned

Scenario 2: Fetch all recipes from RecipeStore with one Recipe
Given the RecipeStore contains Recipe A
When a User fetches all Recipes from the RecipeStore
Then Recipe A is returned from the RecipeStore

Scenario 3: Fetch all recipes from RecipeStore with multiple Recipes
Given the RecipeStore contains Recipe A, B and C
When a User fetches all Recipes from the RecipeStore
Then Recipe A, B and C are returned from the RecipeStore


Story: A User deletes a Recipe

As a user 
I want to delete a Recipe to the RecipeStore
So I can remove Recipies that I no longer want to cook.

Scenario: Delete recipe from RecipeStore
Given the RecipeStore contains Recipe A
When a User delete Recipe A from the RecipeStore
Then the Recipe is deleted from the RecipeStore