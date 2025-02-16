from Seminar915.Seminar9.domain.car import Car
from Seminar915.Seminar9.repository.carsRepositoryInMemory import CarRepositoryInMemory
import pickle

from seminar9.repository.repository import RepositoryError


class CarRepositoryBinary(CarRepositoryInMemory):
    def __init__(self, filename):
        CarRepositoryInMemory.__init__(self)
        #super().__init__()
        self.__filename = filename
        try:
            self.__loadFile()
        except FileNotFoundError:
            raise RepositoryError("The specified binary file was not found")
        except Exception:
            raise RepositoryError("Something went wrong")


    def __saveFile(self):
        file = open(self.__filename, "wb")  # w - write, b - binary
        pickle.dump(self._data, file)
        file.close()

    def __loadFile(self):
        file = open(self.__filename, "rb")  # r - read, b - binary
        self._data = pickle.load(file)
        file.close()

    def addCar(self, car: Car):
        super().addCar(car)
        self.__saveFile()

    def removeCar(self, licensePlate: str) -> Car:
        car = super().removeCar(licensePlate)
        self.__saveFile()
        return car