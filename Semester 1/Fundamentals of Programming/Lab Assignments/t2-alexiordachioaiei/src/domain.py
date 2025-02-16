class OrderError(Exception):
    pass

class Driver(object):
    def __init__(self, driver_id: int, name: str):
        self.id = driver_id
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def __str__(self):
        return f"{self.id}:{self.name}"

class Order(object):
    def __init__(self, driver_id: int, lineage: int):
        self.driver_id = driver_id
        self.lineage = lineage

    @property
    def lineage(self):
        return self.__lineage

    @lineage.setter
    def lineage(self, value):
        if value<1:
            raise OrderError("The distance travelled must be at least 1 km.")
        self.__lineage = value

    @property
    def driver_id(self):
        return self.__driver_id

    @driver_id.setter
    def driver_id(self, value):
        self.__driver_id = value

    def __str__(self):
        return f"{self.driver_id}:{self.lineage}"
