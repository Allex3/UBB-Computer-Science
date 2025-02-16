from enum import Enum

from seminar.group914.seminar_11.repository.repository import Repository


class RepositoryType(Enum):
    MEMORY = 0
    TEXT_FILE = 1
    BINARY_FILE = 2


class Settings:
    # NOTE This class implements the Singleton design pattern (one Pythonic version of it)
    # learn more at https://refactoring.guru/design-patterns/singleton

    # a class-bound field (__instance is not linked to any object of type Settings, but it
    # is linked to the Settings class itself

    __instance = None

    @staticmethod
    def get_instance():
        if Settings.__instance is not None:
            # we return the single Settings object, if it was already created
            return Settings.__instance

        # we create the singular Settgins object here, only if it has not yet been created
        # NOTE We lazy-load the settings file (it means that we only read the actual file when
        # we know that it is required)
        fin = open("settings.properties", "rt")
        file_lines = fin.readlines()
        fin.close()

        settings_dict = {}
        for line in file_lines:
            if line.strip().startswith("#"):
                continue  # move to the next iteration of the innermost loop
            tokens = line.strip().split("=")
            settings_dict[tokens[0].strip()] = tokens[1].strip()

        repo_type = settings_dict["repository"]
        ingredients_file = settings_dict["ingredient_file"]
        recipe_file = settings_dict["recipes_file"]

        repository_type = RepositoryType.MEMORY
        if repo_type == "textfile":
            repository_type = RepositoryType.TEXT_FILE
        elif repo_type == "binaryfile":
            repository_type = RepositoryType.BINARY_FILE

        Settings.__instance = Settings(repository_type, ingredients_file, recipe_file)
        return Settings.__instance

    def __init__(self, repo_type: RepositoryType, ingredients_file: str, recipes_file: str):
        # NOTE The constructor of a class implementing the Singleton design pattern must be
        # marked as private => it cannot be called without get_instance()
        self.__repo_type = repo_type
        self.__ingredients_file = ingredients_file
        self.__recipes_file = recipes_file

    @property
    def repository_type(self):
        return self.__repo_type

    @property
    def ingredients_file(self):
        return self.__ingredients_file

    @property
    def recipes_file(self):
        return self.__recipes_file


settings_one = Settings.get_instance()
settings_two = Settings.get_instance()
# s = Settings("", "", "")
print(id(settings_one), id(settings_two))
print(settings_one.repository_type)
