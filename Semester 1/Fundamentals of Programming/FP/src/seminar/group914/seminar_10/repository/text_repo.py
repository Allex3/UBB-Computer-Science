from datetime import datetime

from seminar.group914.seminar_10.domain.rental import Rental
from seminar.group914.seminar_10.repository.memory_repo import MemoryRepository
from seminar.group914.seminar_9.domain.car import Car


class CarTextFileRepository(MemoryRepository):
    def __init__(self):
        super().__init__()  # calls constructor of base class
        self._file_loaded = False
        # self.__load()

    def add(self, element):
        self.__load()
        super().add(element)
        # if there was no exception, the line below is executed
        self.__save()

    def remove(self, elem_id: int):
        self.__load()
        super().remove(elem_id)
        # if there was no exception, the line below is executed
        self.__save()

    def find(self, elem_id: int):
        self.__load()
        return super().find(elem_id)

    def __iter__(self):
        self.__load()
        return super().__iter__()

    def __len__(self):
        self.__load()
        return super().__len__()

    def __getitem__(self, item):
        self.__load()
        return super().__getitem__()

    def __load(self):
        if self._file_loaded is True:
            return
        self._file_loaded = True
        try:
            fin = open("cars.txt", "rt")
        except FileNotFoundError:
            return

        line = fin.readline()

        while len(line) > 0:
            tokens = line.split(",")
            super().add(Car(int(tokens[0]), tokens[1], tokens[2].strip()))
            line = fin.readline()
        fin.close()

    def __save(self):
        fout = open("cars.txt", "wt")
        for car in self._data.values():
            fout.write(str(car.id) + "," + car.license + "," + car.model + "\r\n")
        fout.close()


class ClientTextFileRepository(MemoryRepository):
    pass


class RentalTextFileRepository(MemoryRepository):
    def __init__(self, car_repo: MemoryRepository, client_repo: MemoryRepository):
        super().__init__()
        self.__car_repo = car_repo
        self.__client_repo = client_repo
        self.__load()

    def add(self, element):
        super().add(element)
        # if there was no exception, the line below is executed
        self.__save()

    def __load(self):
        fin = open("rentals.txt", "rt")
        line = fin.readline()
        while len(line) > 0:
            tokens = line.split(",")
            rental_id = int(tokens[0])
            car_id = int(tokens[1])
            client_id = int(tokens[2])
            start = tokens[3]
            end = tokens[4].strip()

            start_date = datetime.strptime(start, "%Y-%m-%d")
            end_date = datetime.strptime(end, "%Y-%m-%d")

            # NOTE we assume input file are correct :)
            car = self.__car_repo.find(car_id)
            client = self.__client_repo.find(client_id)
            super().add(Rental(rental_id, start_date, end_date, client, car))
            line = fin.readline()
        fin.close()

    def __save(self):
        fout = open("rentals.txt", "wt")
        for rental in self._data.values():
            fout.write(
                str(rental.id) + "," + str(rental.car.id) + "," + str(rental.client.id) + "," + rental.start.strftime(
                    "%Y-%m-%d") + "," + rental.end.strftime("%Y-%m-%d") + "\r\n")
        fout.close()
