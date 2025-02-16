import random

def getRndLetter():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters[random.randint(0, len(letters) - 1)]


def generateLicensePlate():
    return getRndLetter() + getRndLetter() + " " + str(random.randint(10, 99)) + " " + getRndLetter() + getRndLetter() + getRndLetter()


class Car:
    def __init__(self, lPlate: str, brand: str, model: str, color: str):
        self.__licensePlate = lPlate
        self.__brand = brand
        self.__model = model
        self.__color = color

    def getLicensePlate(self):
        return self.__licensePlate

    @property
    def brand(self):
        return self.__brand

    @property
    def model(self):
        return self.__model

    @property
    def color(self):
        return self.__color

    def __str__(self):
        return self.__licensePlate + " " + self.__brand + " " + self.__model + " " + self.__color

def generateNRandomCars(n: int):
    cars = []
    for i in range(n):
        car = Car(generateLicensePlate(), "Volkswagen", "Golf", "White")
        cars.append(car)

    return cars

if __name__=="__main__":
    car = Car("CJ 23 ABC", "Audi", "Model1", "Black")
    car1 = Car(generateLicensePlate(), "Volkswagen", "Golf", "Red")
    print(car1)
    print(car.getLicensePlate())
    print(car.brand)
    #car.brand = "Volkswagen"
    print(car)


