from src.repository import TextRepo

class Services(object):
    def __init__(self, text_repo: TextRepo):
        self.__repo = text_repo

    def add_order(self, driver_id: int, lineage: int):
        """
        Function to add order in the system.
        :param driver_id: The driver's ID
        :param lineage: The order's travelled distance by the driver.
        :return: None
        """
        self.__repo.add_order(driver_id, lineage)

    def get_orders(self):
        return self.__repo.get_orders()

    def get_drivers(self):
        return self.__repo.get_drivers()

    def get_driver_income(self, driver_id: int):
        return self.__repo.compute_income(driver_id)

    def get_driver(self, driver_id: int):
        return self.__repo.get_driver(driver_id)


