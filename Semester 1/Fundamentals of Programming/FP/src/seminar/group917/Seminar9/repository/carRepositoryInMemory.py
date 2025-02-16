from Seminar917.Seminar9.domain.car import Car, generateNCars


class RepositoryError(Exception):
    def __init__(self, msg):
        self.__msg = msg

    def __str__(self):
        return "Repository Error: " + self.__msg

class CarRepositoryInMemory:
    def __init__(self):
        self._data = {}

    def getAllCars(self):
        return list(self._data)

    def addCar(self, car: Car):
        if car.licensePlate in self._data:
            raise RepositoryError("Car is already added")
        self._data[car.licensePlate] = car

    def removeCar(self, licensePlate: str) -> Car:
        """
        TODO Write complete specifications
        :param licensePlate:
        :return:
        """
        if licensePlate not in self._data:
            raise RepositoryError("Car does not exist")
        car = self._data[licensePlate]
        del self._data[licensePlate]
        return car

    def __len__(self):
        return len(list(self._data))

def testInMemoryRepository():
    repo = CarRepositoryInMemory()
    repoLength = 0

    assert len(repo) == repoLength

    cars = generateNCars(5)
    for i in range(5):
        repo.addCar(cars[i])
        repoLength += 1

        assert len(repo) == repoLength

    try:
        repo.addCar(cars[0])
        print("Something is wrong")
        assert False
    except:
        print("Clear")
        assert True

    carToBeDeleted = cars[1]
    deletedCar = repo.removeCar(cars[1].licensePlate)
    assert carToBeDeleted.licensePlate == deletedCar.licensePlate
    assert carToBeDeleted == deletedCar

    #TODO test removing a car that was already removed

#testInMemoryRepository()