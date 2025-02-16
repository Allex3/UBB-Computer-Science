from lecture.livecoding.lecture_9.repo.bakery_memory_repo import BakeryObjectMemoryRepo
from lecture.livecoding.lecture_9.repo.ingredient_text_repo import IngredientTextFileRepo
from lecture.livecoding.lecture_9.repo.recipe_text_repo import RecipeTextFileRepo
from lecture.livecoding.lecture_9.services.services import IngredientService, RecipeService, BakeryProductService
from lecture.livecoding.lecture_9.settings import Settings, RepositoryType
from lecture.livecoding.lecture_9.ui.ui import UserInterface

ingredients_repo = None
recipes_repo = None
products_repo = None

# 1. Start repository layer
if Settings.get_instance().repository_type == RepositoryType.MEMORY:
    # NOTE all domain entities are derived from BakeryObject, so we can use this memory-based
    # repository for all domain entities
    ingredients_repo = BakeryObjectMemoryRepo()
    recipes_repo = BakeryObjectMemoryRepo()
    products_repo = BakeryObjectMemoryRepo()
elif Settings.get_instance().repository_type == RepositoryType.TEXT_FILE:
    ingredients_repo = IngredientTextFileRepo(Settings.get_instance().ingredients_file)
    recipes_repo = RecipeTextFileRepo(Settings.get_instance().recipes_file, ingredients_repo)
    products_repo = BakeryObjectMemoryRepo()  # TODO implement a text-file repository :)
elif Settings.get_instance().repository_type == RepositoryType.BINARY_FILE:
    # TODO implement binary-file based repos
    pass

# 2. Services layer
# NOTE - Repositories are give via constructor parameters
ingredients_service = IngredientService(ingredients_repo)
recipes_service = RecipeService(recipes_repo)
product_service = BakeryProductService(products_repo)

# 3. user interface & start the program
ui = UserInterface(ingredients_service, recipes_service, product_service)
ui.start_ui()
