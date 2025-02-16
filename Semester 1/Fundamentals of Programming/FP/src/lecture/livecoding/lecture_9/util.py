from lecture.livecoding.lecture_9.domain.ingredient import Ingredient
from lecture.livecoding.lecture_9.domain.recipe import Recipe

from lecture.livecoding.lecture_9.repo.bakery_memory_repo import BakeryObjectMemoryRepo
from lecture.livecoding.lecture_9.repo.ingredient_text_repo import IngredientTextFileRepo
from lecture.livecoding.lecture_9.repo.recipe_text_repo import RecipeTextFileRepo


# TODO Ingredient id's must be consistent with those loaded from the ingredient repository
def create_recipes():
    """
    Bread

    1 package (1/4 ounce) active dry yeast
    2-1/4 cups warm water (110° to 115°)
    3 tablespoons sugar plus 1/2 teaspoon sugar
    1 tablespoon salt
    2 tablespoons canola oil
    6-1/4 to 6-3/4 cups bread flour
    source: https://www.tasteofhome.com/recipes/basic-homemade-bread/
    """
    recipe_bread = Recipe(500, "Basic Homemade Bread")
    recipe_bread.ingredients.append(Ingredient(101, "Yeast (dry)", 20))
    recipe_bread.ingredients.append(Ingredient(102, "Sugar (white)", 30))
    recipe_bread.ingredients.append(Ingredient(103, "Salt (regular)", 5))
    recipe_bread.ingredients.append(Ingredient(104, "Oil (canola)", 10))
    recipe_bread.ingredients.append(Ingredient(100, "Bread Flour (White 550)", 1000))

    """
    Cake recipe

    175g (6oz) margarine or softened butter
    175g (6oz) caster sugar
    3 large eggs
    175g (6oz) self-raising flour, sifted
    1tsp baking powder
    1tsp vanilla extract
    pinch of salt
    source: https://www.houseandgarden.co.uk/recipe/simple-vanilla-cake-recipe

    this recipe in CSV file format 
    501,Tasty Cookies,105,175,102,175,106,3, ...
    """
    recipe_cake = Recipe(501, "Tasty Cookies")
    recipe_cake.ingredients.append(Ingredient(105, "Butter", 175))
    recipe_cake.ingredients.append(Ingredient(102, "Sugar (white)", 175))
    recipe_cake.ingredients.append(Ingredient(106, "Egg (chicken)", 3))
    recipe_cake.ingredients.append(Ingredient(107, "Cake flour", 175))
    recipe_cake.ingredients.append(Ingredient(108, "Baking powder", 5))
    recipe_cake.ingredients.append(Ingredient(109, "Vanilla (extract)", 5))
    recipe_cake.ingredients.append(Ingredient(103, "Salt (regular)", 2))

    return [recipe_bread, recipe_cake]


if __name__ == "__main__":
    ingredient_repo = IngredientTextFileRepo()
    recipe_repo = RecipeTextFileRepo(ingredient_repo)

    # recipes_list = create_recipes()
    for recipe in recipe_repo:
        print(recipe)
        # recipe_repo.add(recipe)
