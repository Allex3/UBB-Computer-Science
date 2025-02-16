from seminar10.repository.memory_repo import MemoryRepository
from Seminar917.Seminar10.domain.car import Car
from Seminar917.Seminar10.domain.client import Client

class ClientTextFileRepository(MemoryRepository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__loadFile()

    def __loadFile(self):
        lines = []

        try:
            fin = open(self.__fileName, "rt")
            lines = fin.readlines()
            fin.close()
        except:
            raise ValueError("Load file incomplete")

        for line in lines:
            currentLine = line.split(",")
            newClient = Client(int(currentLine[0].strip()), currentLine[1].strip())
            super().add(newClient)

    def __saveFile(self):
        fout = open(self.__fileName, "wt")

        for client in self:
            clientString = str(client.id) + "," + str(client.name) + "\n"
            fout.write(clientString)

        fout.close()

    def add(self, client: Client):
        super().add(client)
        self.__saveFile()


class CarTextFileRepository(MemoryRepository):
    def __init__(self, fileName):
        super().__init__()
        self.__fileName = fileName
        self.__loadFile()

    def __loadFile(self):
        lines = []

        try:
            fin = open(self.__fileName, "rt")
            lines = fin.readlines()
            fin.close()
        except:
            raise ValueError("Load file incomplete")

        for line in lines:
            currentLine = line.split(",")
            newCar = Car(int(currentLine[0].strip()), currentLine[1].strip(), currentLine[2].strip(),
                         currentLine[3].strip(), currentLine[4].strip())
            super().add(newCar)

    def __saveFile(self):
        fout = open(self.__fileName, "wt")

        for car in self:
            carString = str(car.id) + "," + str(car.licensePlate) + "," + str(car.getCarBrand()) + "," + str(
                car.getCarModel()) + "," + str(car.getCarColor()) + "\n"
            fout.write(carString)

        fout.close()

    def add(self, car: Car):
        super().add(car)
        self.__saveFile()


class RentalRepository(MemoryRepository):
    pass