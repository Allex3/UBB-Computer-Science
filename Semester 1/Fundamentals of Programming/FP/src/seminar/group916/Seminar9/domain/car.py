import random


def getRandomLetter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[random.randint(0, len(letters) - 1)]


def generateLicensePlate():
    return getRandomLetter() + getRandomLetter() + " " + str(random.randint(10, 99)) + " " + getRandomLetter() + getRandomLetter() + getRandomLetter()


class Car:
    def __init__(self, licensePlate: str, brand: str, model: str, color: str):
        self.__licensePlate = licensePlate
        self.__brand = brand
        self.__model = model
        self.__color = color

    def getCarBrand(self):
        return self.__brand

    @property
    def licensePlate(self):
        return self.__licensePlate

    def getCarModel(self):
        return self.__model

    def getCarColor(self):
        return self.__color

    def __str__(self):
        return self.licensePlate + " " + self.__brand + " " + self.__model + " " + self.__color

    def __eq__(self, other):
        # TODO implement this if you want to directly compare objects of type Car
        pass


def generateNRandomCars(n: int):
    cars = []

    for i in range(n):
        car = Car(generateLicensePlate(), "Volkswagen", "Golf", "Pink")
        cars.append(car)

    return cars


if __name__ == "__main__":
    car = Car("CJ 23 ABX", "Audi", "Model1", "Green")

    print(car.getCarBrand())
    print(car.licensePlate)
    #car.licensePlate = "LALA"
