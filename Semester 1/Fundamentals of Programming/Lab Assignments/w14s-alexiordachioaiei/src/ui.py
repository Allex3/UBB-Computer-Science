from datetime import time

from src.repository import RepositoryError
from src.services import Services

class Application:
    def __init__(self, services: Services):
        self.__services = services

        self.__OPTIONS = {"ADD": "1. Add a new flight.",
                          "DISPLAY": "2. Display all flights."}

        self.__ERRORS = {"INVALID": "Invalid input. Try again.",
                         "INT": "Your input was not in integer. Try again!"}

    def __display_flights(self):
        flights = self.__services.get_flights()
        for flight in flights:
            print(flight)
        print()

    def __add_flight(self):
        flight_id = input("Flight id: ")
        depart_city = input("Departure city: ")
        arrival_city = input("Arrival city: ")
        try:
            depart_hour = int(input("Departure hour: "))
            depart_minute = int(input("Departure minute: "))
            arrival_hour = int(input("Arrival hour: "))
            arrival_minute = int(input("Arrival minute: "))

            depart_time = time(depart_hour, depart_minute)
            arrival_time = time(arrival_hour, arrival_minute)

            self.__services.add_flight(flight_id, depart_city, depart_time, arrival_city, arrival_time)

            print("Successfully added flight!")
        except ValueError:
            print(self.__ERRORS["INT"])
            self.__add_flight()
        except RepositoryError as e:
            print(e)



    def run(self):
        while True:
            print(self.__OPTIONS["ADD"])
            print(self.__OPTIONS["DISPLAY"])
            option = input("> ")
            match option:
                case "1":
                    self.__add_flight()
                case "2":
                    self.__display_flights()
                case "0":
                    exit(0)
                case _:
                    print(self.__ERRORS["INVALID"])

