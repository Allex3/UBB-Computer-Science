from lecture.livecoding.lecture_9.domain.bakery_object import BakeryObject
from lecture.livecoding.lecture_9.domain.recipe import Recipe


class BakeryProduct(BakeryObject):
    def __init__(self, object_id: int, name: str, quantity: int, recipe: Recipe):
        super().__init__(object_id, name)
        self.__recipe = recipe
        self.__quantity = quantity

    @property
    def recipe(self):
        return self.__recipe

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_value: int):
        self.__quantity = new_value
