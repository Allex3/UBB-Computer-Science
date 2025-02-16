from Seminar916.Seminar9.domain.car import Car, generateNRandomCars


class RepositoryError(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self):
        return "Repository Exception: " + self.__msg

class CarRepositoryInMemory:
    def __init__(self):
        self._data = {}

    def getAllCars(self):
        return list(self._data)

    def __len__(self):
        return len(list(self._data))

    def addCar(self, car: Car):
        if car.licensePlate in self._data:
            raise RepositoryError("Car already exists")
        self._data[car.licensePlate] = car

    def removeCar(self, licensePlate: str) -> Car:
        if licensePlate not in self._data:
            raise RepositoryError("Car does not exist")

        car = self._data[licensePlate]
        del self._data[licensePlate]

        return car


def testInMemoryRepository():
    repo = CarRepositoryInMemory()
    repoLength = 0

    assert len(repo) == repoLength

    cars = generateNRandomCars(5)
    for i in range(5):
        repo.addCar(cars[i])
        repoLength += 1

        assert len(repo) == repoLength

    try:
        repo.addCar(cars[0])
        print("We have a problem")
        assert False
    except:
        print("Clear")
        assert True

    carToBeDeleted = cars[1]
    deletedCar = repo.removeCar(cars[1].licensePlate)
    assert deletedCar.licensePlate == carToBeDeleted.licensePlate

testInMemoryRepository()