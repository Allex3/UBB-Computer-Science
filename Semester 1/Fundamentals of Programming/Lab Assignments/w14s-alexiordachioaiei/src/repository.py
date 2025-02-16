from datetime import time, datetime, date

from src.domain import FlightInfo


class RepositoryError(Exception):
    pass


class FlightsRepo:
    def __init__(self, text_file: str = "flights.txt"):
        self.__text_file = text_file
        self.__flights: dict[str, FlightInfo] = {}
        self.__arrivals: dict[str, list[time]] = {}
        self.__departures: dict[str, list[time]] = {}
        self.__load()

    def __load(self):
        file = open(self.__text_file, "r")
        if file.read() == "":
            file.close()
            raise RepositoryError("File is empty or does not exist!")

        file.close()

        file = open(self.__text_file, "r")
        lines = file.readlines()

        for line in lines:
            info_line = line.strip('\n').split(',')
            flight_id = info_line[0]
            depart_city = info_line[1]
            depart_time = time(int(info_line[2].split(":")[0]), int(info_line[2].split(":")[1]))
            arrival_city = info_line[3]
            arrival_time = time(int(info_line[4].split(":")[0]), int(info_line[4].split(":")[1]))
            flight_info = FlightInfo(flight_id, depart_city, depart_time, arrival_city, arrival_time)
            self.__flights[flight_id] = flight_info

            if depart_city not in self.__departures: # City key does not exist yet as a departure, initialize an empty list for it
                self.__departures[depart_city] = []
            if arrival_city not in self.__arrivals:
                self.__arrivals[arrival_city] = []

            self.__departures[depart_city].append(depart_time)
            self.__arrivals[arrival_city].append(arrival_time)

        file.close()

    def __save(self):
        file = open(self.__text_file, "w")
        for flight in self.__flights.values():
            file.write(str(flight)+'\n')

        file.close()

    def get_flights(self):
        return list(self.__flights.values())

    def add_flight(self, flight_id: str, depart_city: str, depart_time: time, arrival_city: str, arrival_time: time):
        if flight_id in self.__flights:
            raise RepositoryError("Flight already exists!")

        flight_time = (datetime.combine(date.today(), arrival_time) - datetime.combine(date.today(), depart_time))
        if not (15<=(flight_time.seconds / 60) <=90): # Flight between 15 and 90 minutes
            raise RepositoryError("Flight time is out of range! (It should be 15 to 90 minutes)")

        # Check that the airports does not have any departures or arrivals at the same minute!
        if depart_city in self.__departures:
            if depart_time in self.__departures[depart_city]: # Time of a departure at the same minute exists
                raise RepositoryError("Departure time is already taken!")

        if arrival_city in self.__arrivals:
            if arrival_time in self.__arrivals[arrival_city]:
                raise RepositoryError("Arrival time is already taken!")

        self.__flights[flight_id] = FlightInfo(flight_id, depart_city, depart_time, arrival_city, arrival_time)

        if depart_city not in self.__departures:  # City key does not exist yet as a departure, initialize an empty list for it
            self.__departures[depart_city] = []
        if arrival_city not in self.__arrivals:
            self.__arrivals[arrival_city] = []

        self.__departures[depart_city].append(depart_time)
        self.__arrivals[arrival_city].append(arrival_time)





        self.__save()