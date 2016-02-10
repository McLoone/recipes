#Recipes is a very small recipe backend.#

To build the docker image: 
  docker build -t mcloone/recipes .
  
To run the docker container:
  docker run -d -p 8080:8080 mcloone/recipes
  
Example call to a rest endpoint:
    curl http://<docker-ip>:8080/recipes

**Story:** A User add a Recipe

As a user<br/>
I want to add a Recipe to the RecipeStore<br/>
So I can fetch it when I want to cook some dinner<br/>

**Scenario:** Add recipe to RecipeStore<br/>
**Given** the RecipeStore is empty<br/>
**When** a User add a Recipe<br/>
**Then** the Recipe is added to the RecipeStore<br/>


**Story:** A User retrieves Recipes from RecipeStore<br/>

As a user<br/>
I want to fetch all available Recipes from the RecipeStore<br/>
So I can choose a meal to cook<br/>

**Scenario 1:** Fetch all recipes from empty RecipeStore<br/>
**Given** the RecipeStore is empty<br/>
**When** a User fetches all Recipes from the RecipeStore<br/>
**Then** no Recipes are returned<br/>

**Scenario 2:** Fetch all recipes from RecipeStore with one Recipe<br/>
**Given** the RecipeStore contains Recipe A<br/>
**When** a User fetches all Recipes from the RecipeStore<br/>
**Then** Recipe A is returned from the RecipeStore<br/>

**Scenario 3:** Fetch all recipes from RecipeStore with multiple Recipes<br/>
**Given** the RecipeStore contains Recipe A, B and C<br/>
**When** a User fetches all Recipes from the RecipeStore<br/>
**Then** Recipe A, B and C are returned from the RecipeStore<br/>


**Story:** A User deletes a Recipe<br/>

As a user<br/>
I want to delete a Recipe to the RecipeStore<br/>
So I can remove Recipies that I no longer want to cook.<br/>

**Scenario:** Delete recipe from RecipeStore<br/>
**Given** the RecipeStore contains Recipe A<br/>
**When** a User delete Recipe A from the RecipeStore<br/>
**Then** the Recipe is deleted from the RecipeStore<br/>