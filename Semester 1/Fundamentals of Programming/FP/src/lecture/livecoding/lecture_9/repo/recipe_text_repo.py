from lecture.livecoding.lecture_9.domain.bakery_object import BakeryObject
from lecture.livecoding.lecture_9.domain.ingredient import Ingredient
from lecture.livecoding.lecture_9.domain.recipe import Recipe
from lecture.livecoding.lecture_9.repo.bakery_memory_repo import BakeryObjectMemoryRepo


class RecipeTextFileRepo(BakeryObjectMemoryRepo):
    def __init__(self, file_name: str, ingredient_repo: BakeryObjectMemoryRepo):
        super().__init__()
        self.__file_name = file_name
        self.__ingredient_repo = ingredient_repo
        self.__load()

    def __load(self):
        fin = open(self.__file_name, "rt")
        line = fin.readline()
        while len(line) > 0:
            tokens = line.split(",")
            recipe_id = int(tokens[0])  # NOTE assume input files are a-ok
            recipe_name = tokens[1]

            recipe = Recipe(recipe_id, recipe_name)

            for index in range(2, len(tokens), 2):
                ingredient_id = int(tokens[index])
                ingredient_quantity = int(tokens[index + 1])
                ingredient_name = self.__ingredient_repo.find(ingredient_id).name
                # NOTE Build a new Ingredient as the quantities are different
                ingredient = Ingredient(ingredient_id, ingredient_name, ingredient_quantity)
                recipe.ingredients.append(ingredient)

            super().add(recipe)
            line = fin.readline()
        fin.close()

    def add(self, bakery_object: BakeryObject):
        super().add(bakery_object)
        self.__save()

    def __save(self):
        fout = open(self.__file_name, "wt")
        for r in self._data.values():
            recipe_str = f"{r.id},{r.name},"
            for ingredient in r.ingredients:
                recipe_str += str(ingredient.id) + ","
                recipe_str += str(ingredient.quantity) + ","
            fout.write(recipe_str.strip(",") + "\r\n")
        fout.close()
