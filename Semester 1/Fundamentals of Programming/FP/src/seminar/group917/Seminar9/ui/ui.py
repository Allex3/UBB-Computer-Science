from Seminar917.Seminar9.repository.carRepositoryBinary import CarRepositoryBinary
from Seminar917.Seminar9.domain.car import Car

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

            try:
                choice = input("Your choice: ")
                if choice == "0":
                    break
                elif choice == "1":
                    licensePlate = input("License Plate: ")
                    brand = input("Brand: ")
                    model = input("Model: ")
                    color = input("Color: ")
                    self.__repo.addCar(Car(licensePlate, brand, model, color))
                elif choice == "2":
                    licensePlate = input("License Plate: ")
                    self.__repo.removeCar(licensePlate)
                elif choice == "3":
                    print(self.__repo.getAllCars())
                else: continue
            except Exception as e:
                print(e)

if __name__=="__main__":
    ui = UI()
    ui.start()