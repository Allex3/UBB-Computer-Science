from datetime import time

class FlightInfo:
    def __init__(self, id: str, depart_city: str, depart_time: time, arrival_city: str, arrival_time: time):
        self.id = id
        self.depart_city = depart_city
        self.depart_time = depart_time
        self.arrival_city = arrival_city
        self.arrival_time = arrival_time

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def depart_city(self):
        return self.__depart_city

    @depart_city.setter
    def depart_city(self, value: str):
        self.__depart_city = value

    @property
    def depart_time(self):
        return self.__depart_time

    @depart_time.setter
    def depart_time(self, value: time):
        self.__depart_time = value

    @property
    def arrival_city(self):
        return self.__arrival_city

    @arrival_city.setter
    def arrival_city(self, value: str):
        self.__arrival_city = value

    @property
    def arrival_time(self):
        return self.__arrival_time

    @arrival_time.setter
    def arrival_time(self, value: time):
        self.__arrival_time = value

    def __str__(self):
        return f"{self.id},{self.depart_city},{self.depart_time.strftime('%H:%M')},{self.arrival_city},{self.arrival_time.strftime('%H:%M')}"

