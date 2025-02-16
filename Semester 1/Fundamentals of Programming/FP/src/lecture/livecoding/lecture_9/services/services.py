from lecture.livecoding.lecture_9.domain.bakery_product import BakeryProduct
from lecture.livecoding.lecture_9.repo.bakery_memory_repo import BakeryObjectMemoryRepo


class IngredientService:
    def __init__(self, repository: BakeryObjectMemoryRepo):
        self.__repo = repository


class RecipeService:
    def __init__(self, repository: BakeryObjectMemoryRepo):
        self.__repo = repository


class BakeryProductService:
    def __init__(self, repository: BakeryObjectMemoryRepo):
        self.__repo = repository

    def add(self, bakery_product: BakeryProduct):
        pass

    def bake(self, bakery_product: BakeryProduct, quantity: int):
        pass
