from Seminar916.Seminar9.repository.carRepositoryBinary import CarRepositoryBinary
from Seminar916.Seminar9.domain.car import Car
from Seminar916.Seminar9.repository.carRepositoryInMemory import RepositoryError


class UI:
    def __init__(self):
        self.__repo = CarRepositoryBinary("cars.pickle")

    def printMenu(self):
        print("0. Exit")
        print("1. Add car")
        print("2. Remove car")
        print("3. See all cars")

    def start(self):
        while True:
            self.printMenu()

            choice = input("Your choice: ")

            if choice == "0":
                break
            elif choice == "1":
                try:
                    licensePlate = input("License Plate: ")
                    brand = input("Brand: ")
                    model = input("Model: ")
                    color = input("Color: ")

                    self.__repo.addCar(Car(licensePlate, brand, model, color))
                except RepositoryError as e:
                    print(e)

            elif choice == "2":
                try:
                    licensePlate = input("License Plate: ")
                    self.__repo.removeCar(licensePlate)
                except RepositoryError as e:
                    print(e)
            elif choice == "3":
                print(self.__repo.getAllCars())
            else:
                continue

if __name__=="__main__":
    ui = UI()
    ui.start()