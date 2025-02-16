from seminar.group914.seminar_9.domain.car import Car


class RepositoryError(Exception):
    # this means that class RepositoryError is inherited from Python's default Exception class
    # What does this mean?
    #   1. We can say that a RepositoryError is also an Exception
    #   2. The RepositoryError has all the non-private fields and methods of Exception
    #   3. Usually, wherever you can use an Exception, you can also use a RepositoryError
    #   4. We can use separate except branches for each Exception type
    # It's easier to work with larger programs when we have our own exception types
    def __init__(self, message: str = ""):
        self.__message = message

    @property
    def message(self):
        return self.__message


class CarMemoryRepo:
    # repository class to keep car instances in memory
    # Any problems?
    #   1. It can only store cars :( because we access car.id
    #   2. Does not save cars anywhere, data is lost when program is stopped

    def __init__(self):
        self._data = {}  # unless we specify key:value, this is a set

    def add(self, car: Car):
        """
        Adds the given car to the repo
        :param car:
        :return:
        :raises: RepositoryError in case of duplicate car ID
        """
        if car.id in self._data:
            raise RepositoryError("Duplicate car ID")
        # associate value car with key car.id
        self._data[car.id] = car  # <=> self.__data.put(car.id,car)

    def delete(self, car_id: int):
        """
        Delete given car from repo
        :param car_id:
        :return:
        :raises: RepositoryError in case car with given id not found
        """
        if car_id not in self._data:
            raise RepositoryError(f"car ID {car_id} not found!")
        self._data.pop(car_id)

    def find(self, car_id: int) -> Car:  # alternate return types
        """
        Search for the car with given id
        :param car_id:
        :return: Return the car, None if car not found
        """
        if car_id not in self._data:
            return None
        return self._data[car_id]

    def __len__(self):
        return len(self._data)


"""
    Once we have a class's specification, we can write a test for it :)
"""


def test_car_memory_repo():
    repo = CarMemoryRepo()
    assert len(repo) == 0

    car_1 = Car(100, "CJ 01 RTY", "Toyota Corolla")
    repo.add(car_1)
    assert len(repo) == 1
    car_2 = Car(101, "AB 01 RTY", "Dacia Jogger")
    repo.add(car_2)
    assert len(repo) == 2

    # try to add a car that is already in the repo
    try:
        repo.add(car_1)
        assert False  # we expect an exception on the previous line
    except RepositoryError:
        assert len(repo) == 2

    assert repo.find(100) == car_1
    assert repo.find(101) == car_2
    repo.delete(100)
    assert len(repo) == 1


test_car_memory_repo()
