from Seminar916.Seminar10.domain.car import Car

class RepositoryError(Exception):
    pass


class DuplicateIDError(RepositoryError):
    pass


class IDNotFoundError(RepositoryError):
    pass


class RepositoryIterator():
    def __init__(self, data):
        self.__data = data
        self.__pos = -1

    def __next__(self):
        self.__pos += 1
        if len(self.__data) == self.__pos:
            # we have run out of elements in the data structure
            raise StopIteration()

        return self.__data[self.__pos]


class MemoryRepository:
    def __init__(self):
        self._data = {}  # _data is protected => classes derived from IngredientMemoryRepo can access it

    def add(self, element):
        # dictionary means (key, value) pairs where keys are immutable and unique
        if element.id in self._data:
            raise DuplicateIDError("Duplicate object ID")
        self._data[element.id] = element

    def remove(self, elem_id: int):
        if elem_id not in self._data:  # is the elem_id already a key in the dict?
            raise IDNotFoundError("ID not found")
        return self._data.pop(elem_id)

    def find(self, elem_id: int):
        if elem_id not in self._data:  # is the elem_id already a key in the dict?
            return None
        return self._data[elem_id]

    def __iter__(self):
        # create an iterator for the repository
        # https://refactoring.guru/design-patterns/iterator
        return RepositoryIterator(list(self._data.values()))

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        if item not in self._data:
            return None
        return self._data[item]

if __name__=="__main__":
    repo =  MemoryRepository()
    car1 = Car(99, "BN 99 USB", "Dacia", "Sandero", "pink")
    car2 = Car(98, "BN 98 USB", "Dacia", "Sandero", "pink")
    car3 = Car(97, "BN 97 USB", "Dacia", "Sandero", "pink")
    car4 = Car(96, "BN 96 USB", "Dacia", "Sandero", "pink")

    repo.add(car1)
    repo.add(car2)
    repo.add(car3)
    repo.add(car4)

    for car in repo:
        print(car)