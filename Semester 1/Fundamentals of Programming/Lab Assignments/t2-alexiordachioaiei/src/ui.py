from src.services import Services
from src.repository import RepositoryError
from src.domain import OrderError

class ApplicationUI(object):
    def __init__(self, services: Services):
        self.__services = services

        self.__UI = {"INTRODUCTION": "This app manages a company's drivers' orders. Select an option from the list below.\n",
                     "ADD_ORDER": "1. Add an order into the system.",
                     "DISPLAY_ALL": "2. Display all driver and order information.",
                     "INCOME": "3. Compute the total income of a driver given their ID and display the driver's ID and name.",
                     "EXIT": "0. Exit the application.",}

        self.__ADD_ORDER = "1"
        self.__DISPLAY_ALL = "2"
        self.__INCOME = "3"
        self.__EXIT = "0"

        self.__ERRORS = {"INT": "The driver's ID should be an integer."}

    def __print_introduction(self):
        print(self.__UI["INTRODUCTION"])

    def __print_menu(self):
        print(self.__UI["ADD_ORDER"])
        print(self.__UI["DISPLAY_ALL"])
        print(self.__UI["INCOME"])
        print(self.__UI["EXIT"])

    def __get_driver_id(self):
        try:
            driver_id = int(input("Driver id: "))
            return driver_id
        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_driver_id()

    def __get_order_lineage(self):
        try:
            order_lineage = int(input("Order lineage: "))
            return order_lineage
        except ValueError:
            print(self.__ERRORS["INT"])
            return self.__get_order_lineage()

    def __add_order(self, driver_id: int, lineage: int):
        try:
            self.__services.add_order(driver_id, lineage)
        except RepositoryError as e:
            print(e)
        except OrderError as e:
            print(e)

    def __display_all(self):
        drivers = self.__services.get_drivers()
        orders = self.__services.get_orders()
        print("Drivers information:\n")
        for driver in drivers.values():
            print(driver)

        print("\n\nOrder information:\n")
        for order in orders:
            print(order)

    def __display_income(self, driver_id):
        try:
            driver_income = self.__services.get_driver_income(driver_id)
            driver = self.__services.get_driver(driver_id)
            print(f"The driver with ID {driver.id} by the name of {driver.name} has an income of {driver_income} RON.")
        except RepositoryError as e:
            print(e)

    def run(self):
        self.__print_menu()
        while True:
            option = input("> ")
            match option:
                case "1":
                    driver_id = self.__get_driver_id()
                    lineage = self.__get_order_lineage()
                    self.__add_order(driver_id, lineage)
                case "2":
                    self.__display_all()
                case "3":
                    driver_id = self.__get_driver_id()
                    self.__display_income(driver_id)
                case "0":
                    exit(0)

