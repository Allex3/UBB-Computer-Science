from unittest import TestCase

from lecture.livecoding.lecture_9.domain.ingredient import Ingredient
from lecture.livecoding.lecture_9.repo.bakery_memory_repo import BakeryObjectMemoryRepo


class TestBakeryMemoryRepo(TestCase):
    def test_repo(self):
        repo = BakeryObjectMemoryRepo()
        self.assertEqual(len(repo), 0)
        repo.add(Ingredient(100, "Sugar", 100))
        repo.add(Ingredient(101, "Spice", 100))
        self.assertEqual(len(repo), 2)
