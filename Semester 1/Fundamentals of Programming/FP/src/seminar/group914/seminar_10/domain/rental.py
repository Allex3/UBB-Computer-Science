from datetime import date, timedelta

from seminar.group914.seminar_10.domain.client import Client
from seminar.group914.seminar_9.domain.car import Car


class Rental:
    def __init__(self, rental_id: int, start: date, end: date, client, car):
        self.__id = rental_id
        self.__client = client
        self.__car = car
        self.__start = start
        self.__end = end

    @property
    def id(self):
        return self.__id

    @property
    def client(self):
        return self.__client

    @property
    def car(self):
        return self.__car

    @property
    def start(self):
        return self.__start

    @property
    def end(self):
        return self.__end

    # len(rental)
    def __len__(self):
        if self.__end is not None:
            return (self.__end - self.__start).days + 1
        today = date.today()
        return (today - self.__start).days + 1

    def __repr__(self):
        return str(self)

    def __str__(self):
        # return
        from_date = self.__start.strftime("%Y-%m-%d")
        to_date = self.__end.strftime("%Y-%m-%d")
        return f"{self.id} - [car {self.car}] - [client {self.client}] - from {from_date} to {to_date}"


if __name__ == "__main__":
    d1 = date(2020, 12, 15)
    d2 = date(2022, 12, 15)

    car = Car(100, "AB 01 ERT", "VW Tiguan")
    client = Client(200, "Popescu Marcel")
    rent = Rental(300, date(2024, 11, 30), date(2024, 12, 5), client, car)

    print(rent)
