from repository import FlightsRepo


class Services:
    def __init__(self, repo: FlightsRepo):
        self.__repo = repo

    def get_flights(self):
        return self.__repo.get_flights()

    def add_flight(self, flight_id, depart_city, depart_time, arrival_city, arrival_time):
        self.__repo.add_flight(flight_id, depart_city, depart_time, arrival_city, arrival_time)
