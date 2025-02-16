from src.domain import Order, Driver

class RepositoryError(Exception):
    pass

class MemoryRepo(object):
    def __init__(self):
        self._drivers: dict[int, Driver] = {}
        self._orders: list[Order] = []

    def get_drivers(self):
        return self._drivers

    def get_orders(self):
        return self._orders

    def get_driver(self, driver_id):
        if driver_id not in self._drivers:
            raise RepositoryError(f"The driver with ID {driver_id} does not exist.")

        return self._drivers[driver_id]


    def add_order(self, driver_id: int, lineage: int):
        """
        Function to add order in the system.
        :param driver_id: The driver's ID
        :param lineage: The order's travelled distance by the driver.
        :return: None
        """
        if driver_id not in self._drivers:
            raise RepositoryError(f"The driver with ID {driver_id} does not exist.")
        self._orders.append(Order(driver_id, lineage))

    def add_driver(self, driver_id: int, name: str):
        self._drivers[driver_id] = Driver(driver_id, name)

    def compute_income(self, driver_id: int):
        if driver_id not in self._drivers:
            raise RepositoryError(f"The driver with ID {driver_id} does not exist.")

        driver_income = 0
        for order in self._orders:
            if order.driver_id == driver_id:
                driver_income += 2.5 * order.lineage

        return driver_income

class TextRepo(MemoryRepo):
    def __init__(self, orders_file_name: str = "orders.txt", drivers_file_name: str = "drivers.txt"):
        super().__init__()
        self.__orders_file_name = orders_file_name
        self.__drivers_file_name = drivers_file_name
        self.__load()

    def __load(self):
        """
        Function to load the drivers and orders from the text files into memory.
        :return: None
        """
        drivers_file = open(self.__drivers_file_name, "r")
        lines = drivers_file.readlines()
        for line in lines:
            line = line.strip("\n").split(":")
            driver_id = int(line[0])
            name = line[1]
            super().add_driver(driver_id, name)

        drivers_file.close()

        orders_file = open(self.__orders_file_name, "r")
        lines = orders_file.readlines()
        for line in lines:
            line = line.strip("\n").split(":")
            driver_id = int(line[0])
            lineage = int(line[1])
            super().add_order(driver_id, lineage)

        orders_file.close()

    def __save_orders(self):
        """
        Function to save the orders after we added/removed one, into the text file.
        :return: None
        """
        orders_file = open(self.__orders_file_name, "w")
        for order in self._orders:
            orders_file.write(f"{order}\n")

        orders_file.close()

    def add_order(self, driver_id: int, lineage: int):
        """
        Function to add order in the system's text file.
        :param driver_id: The driver's ID
        :param lineage: The order's travelled distance by the driver.
        :return: None
        """
        super().add_order(driver_id, lineage)
        self.__save_orders()

    def compute_income(self, driver_id: int):
        return super().compute_income(driver_id)


