from lecture.livecoding.lecture_9.domain.bakery_object import BakeryObject


class Ingredient(BakeryObject):
    def __init__(self, ingredient_id: int, name: str, quantity: int):
        super().__init__(ingredient_id, name)
        self.__quantity = quantity

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, new_quantity):
        self.__quantity = new_quantity

    def __str__(self):
        # super() - goes to the base class of this
        # return super().__str__() + "abcd"
        return f"Ingredient id={self.id} is {self.name}, quantity={self.quantity}"
