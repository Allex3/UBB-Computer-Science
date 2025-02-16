from lecture.livecoding.lecture_9.domain.bakery_object import BakeryObject
from lecture.livecoding.lecture_9.domain.ingredient import Ingredient
from lecture.livecoding.lecture_9.repo.bakery_memory_repo import BakeryObjectMemoryRepo, RepositoryError


class IngredientTextFileRepo(BakeryObjectMemoryRepo):
    def __init__(self, file_name: str):
        super().__init__()
        self.__file_name = file_name
        self.__load_file()

    def add(self, bakery_object: Ingredient):
        super().add(bakery_object)
        # if super().add(...) was successful we save the file with the updated ingredients
        self.__save_file()

    def remove(self, bakery_object_id: int) -> BakeryObject:
        bakery_object = super().remove(bakery_object_id)
        self.__save_file()
        return bakery_object

    def __load_file(self):
        fin = open(self.__file_name, "rt")
        line = fin.readline()
        while len(line) > 0:
            tokens = line.split(",")
            super().add(Ingredient(int(tokens[0]), tokens[1].strip(), int(tokens[2])))
            line = fin.readline()

    def __save_file(self):
        fout = open(self.__file_name, "wt")  # w - write, t - text
        for ingr in self._data.values():
            fout.write(str(ingr.id) + "," + ingr.name + "," + str(ingr.quantity) + "\r\n")
            fout.close()


if __name__ == "__main__":
    try:
        repo = IngredientTextFileRepo()
        # repo.add(Ingredient(100, "Sugar"))

        for ingredient in repo:
            print(ingredient)

    except FileNotFoundError as e:
        print("yep!")
    except RepositoryError as e:
        print(e)
