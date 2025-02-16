from lecture.livecoding.lecture_9.domain.bakery_object import BakeryObject
from lecture.livecoding.lecture_9.domain.ingredient import Ingredient


class Recipe(BakeryObject):
    def __init__(self, object_id: int, name: str):
        super().__init__(object_id, name)
        self.__ingredients = []

    def add_ingredient(self, ingredient: Ingredient):
        self.__ingredients.append(ingredient)

    @property
    def ingredients(self):
        """
        Returns a reference to the LIVE LIST of ingredients
        :return: The list of ingredients
        """
        return self.__ingredients

    def __str__(self):
        s = f"Recipe {self.id} - {self.name}:\r\n"
        for ingr in self.ingredients:
            s += str(ingr) + "\r\n"
        return s
