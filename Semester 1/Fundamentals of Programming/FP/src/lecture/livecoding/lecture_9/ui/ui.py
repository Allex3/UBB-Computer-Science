from lecture.livecoding.lecture_9.services.services import IngredientService, RecipeService, BakeryProductService


class UserInterface:
    def __init__(self, ingredient_service: IngredientService, recipe_service: RecipeService,
                 product_service: BakeryProductService):
        # NOTE - The user interface depends on the the services for ingredient, recipe, product
        # By providing the required objects as parameters to the constructor, we make sure that
        # we cannot build a UserInterface object without all its dependencies

        # NOTE Passing dependencies as constructor parameters is a basic means of dependency injection
        # 'dependency injection' - we inject the classes we need through the __init__ call
        # NOTE We should be able to change the dependencies without altering the code of the UI class
        self.__ingredient_service = ingredient_service
        self.__recipe_service = recipe_service
        self.__product_service = product_service

    def start_ui(self):
        # NOTE This is where we start the program's user interface
        pass
