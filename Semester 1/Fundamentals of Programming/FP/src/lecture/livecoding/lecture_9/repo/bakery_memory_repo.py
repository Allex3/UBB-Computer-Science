from lecture.livecoding.lecture_9.domain.bakery_object import BakeryObject


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


class BakeryObjectMemoryRepo:
    def __init__(self):
        self._data = {}  # _data is protected => classes derived from IngredientMemoryRepo can access it

    def add(self, bakery_object: BakeryObject):
        # dictionary means (key, value) pairs where keys are immutable and unique
        if bakery_object.id in self._data:
            raise DuplicateIDError("Duplicate ingredient ID")
        self._data[bakery_object.id] = bakery_object

    def remove(self, bakery_object_id: int) -> BakeryObject:
        if bakery_object_id not in self._data:
            # NOTE creating and raising exceptions is sloooooooow
            raise IDNotFoundError("ID not found")
        return self._data.pop(bakery_object_id)

    def find(self, bakery_object_id: int):
        if bakery_object_id not in self._data:  # is the ingr_id already a key in the dict?
            return None
        return self._data[bakery_object_id]

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
