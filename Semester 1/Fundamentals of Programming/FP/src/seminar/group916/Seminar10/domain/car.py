import random

def getRndLetter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[random.randint(0, len(letters) - 1)]


def generateLicensePlate():
    return getRndLetter() + getRndLetter() + " " + str(random.randint(10, 99)) + " " + getRndLetter() + getRndLetter() + getRndLetter()


class Car:
    def __init__(self, carId, licensePlate: str, brand: str, model: str, color: str):
        self.__id = carId
        self.__licensePlate = licensePlate
        self.__brand = brand
        self.__model = model
        self.__color = color

    @property
    def id(self):
        return self.__id

    @property
    def licensePlate(self):
        return self.__licensePlate

    def getCarBrand(self):
        return self.__brand

    def getCarModel(self):
        return self.__model

    def getCarColor(self):
        return self.__color

    def __eq__(self, other):
        return self.licensePlate == other.licensePlate

    def __str__(self):
        return str(self.__id) + " " + self.__licensePlate + " " + self.__brand + " " + self.__model + " " + self.__color

def generateNCars(n: int):
    cars = []
    for i in range(n):
        car = Car(generateLicensePlate(), "Volkswagen", "Golf", "Gray")
        cars.append(car)

    return cars

if __name__=="__main__":
    car = Car(1, "CJ 12 ABC", "Audi", "Model1", "Black")
    print(car)
    print(car.licensePlate)
    #car.licensePlate = "LALALa"
