from unittest import TestCase

from lecture.livecoding.lecture_9.domain.ingredient import Ingredient


class TestIngredient(TestCase):

    def test_ingredient(self):
        ingr = Ingredient(100, "Sugar", 100)
        self.assertEqual(ingr.id, 101)
        self.assertEqual(ingr.name, "Sugar")

    def test_ingredient_quantity(self):
        ingr = Ingredient(100, "Sugar", 100)
        self.assertEqual(ingr.quantity, 100)
