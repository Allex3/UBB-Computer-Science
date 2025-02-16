from Seminar915.Seminar9.domain.car import Car, generateNRandomCars


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

    def addCar(self, car: Car):
        if car.getLicensePlate() in self._data:
            raise RepositoryError("Car already exists")
        self._data[car.getLicensePlate()] = car

    def removeCar(self, licensePlate: str) -> Car:
        if licensePlate not in self._data:
            raise RepositoryError("Car does not exist")

        car = self._data[licensePlate]
        del self._data[licensePlate]
        return car

    def __len__(self):
        return len(list(self._data))

def testInMemory():
    repo = CarRepositoryInMemory()
    repo_len = 0

    assert len(repo) == repo_len

    cars = generateNRandomCars(5)
    for i in range(len(cars)):
        repo.addCar(cars[i])
        repo_len += 1

        assert len(repo) == repo_len

    try:
        repo.addCar(cars[0])
        repo_len += 1
        assert False
    except:
        assert len(repo) == repo_len

    carToDelete = cars[1]
    deletedCar = repo.removeCar(carToDelete.getLicensePlate())
    repo_len -= 1

    assert len(repo) == repo_len
    assert carToDelete.getLicensePlate() == deletedCar.getLicensePlate()

testInMemory()

