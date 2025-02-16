import pickle

from seminar.group914.seminar_9.domain.car import Car
from seminar.group914.seminar_9.repository.repo_memory import CarMemoryRepo


class CarBinaryRepo(CarMemoryRepo):
    """
    1. We already have class CarMemoryRepo which does almost everything we need (except save/load file)
    2. We want to be able to use both memory and binary file repos (inheritance)
    3. We want to reuse the code that we already have (inheritance)

    What we'll do:
        - Reuse already written code by inheriting from the CarMemoryRepo class
        - Add code to save/load binary files
        - Make the file-based repository work transparently to the user
    """

    def __init__(self, file_name: str = "cars.bin"):
        super().__init__()  # super() goes to the super class
        self.__file_name = file_name
        self.__load()

    def __load(self):
        try:
            fin = open(self.__file_name, "rb")
            self._data = pickle.load(fin)
            fin.close()
        except FileNotFoundError:
            # In case the file was not found, it means there were no cars to load
            # File will be created on save
            pass

    def __save(self):
        fout = open(self.__file_name, "wb")  # w - write, b - binary
        pickle.dump(self._data, fout)
        fout.close()

    def add(self, car: Car):
        # this calls the add() method in class CarMemoryRepo
        super().add(car)
        # in case the line raised a RepositoryError, we do not need to save the file as no change has taken
        # place; since there's not try ... except block here, the method exits with exception

        # if everything is fine, save the cars to the file
        self.__save()


if __name__ == "__main__":
    # c = Car(100, "SJ 85 ERT", "green")
    # data = [c, c, c]
    # #
    # fout = open("cars.bin", "wb")  # w - write, b - binary
    # pickle.dump(data, fout)
    # fout.close()

    # fin = open("cars.bin", "rb")
    # data = pickle.load(fin)
    # print(type(data))
    # print(data)

    repo = CarBinaryRepo()
    #
    repo.add(Car(100, "AB 44 QWE", "red"))
    print(len(repo))

    # repo.add(Car(100, "AB 44 QWE", "red"))
