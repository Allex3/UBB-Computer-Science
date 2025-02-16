import pickle

from Seminar915.Seminar9.repository.carsRepositoryInMemory import RepositoryError
from Seminar916.Seminar9.domain.car import Car
from Seminar916.Seminar9.repository.carRepositoryInMemory import CarRepositoryInMemory


class CarRepositoryBinary(CarRepositoryInMemory):
    def __init__(self, filename):
        CarRepositoryInMemory.__init__(self)
        #super().__init__()
        self.__filename = filename
        try:
            self.__loadData()
        except FileNotFoundError:
            raise RepositoryError("File was not found")
        except Exception:
            raise RepositoryError("Something went wrong")

    def __loadData(self):
        file = open(self.__filename, "rb") # r - read, b - binary
        self._data = pickle.load(file)
        file.close()

    def __saveData(self):
        file = open(self.__filename, "wb") # w - write, b - binary
        pickle.dump(self._data, file)
        file.close()

    def addCar(self, car: Car):
        super().addCar(car)
        self.__saveData()

    def removeCar(self, licensePlate: str) -> Car:
        super().removeCar(licensePlate)
        self.__saveData()