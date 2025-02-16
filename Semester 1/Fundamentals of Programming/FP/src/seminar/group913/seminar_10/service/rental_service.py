from seminar.group913.seminar_10.domain.rental import Rental
from seminar.group913.seminar_10.repository.memory_repo import MemoryRepository
from seminar.group913.seminar_9.domain.car import Car


class CarPopularityDTO:  # DTO - data transfer object
    def __init__(self, car: Car, client_count: int):
        self.__car = car
        self.__client_count = client_count

    @property
    def car(self):
        return self.__car

    @property
    def clients(self):
        return self.__client_count

    def __lt__(self, other):
        return self.__client_count > other.__client_count


class RentalService:
    def __init__(self, repo: MemoryRepository, car_repo: MemoryRepository):
        self._repo = repo
        self.__car_repo = car_repo

    def get(self, rental_id: int) -> Rental:
        return self._repo[rental_id]

    def most_popular_cars(self) -> [CarPopularityDTO]:
        """
        Return a list of cars with the number of distinct clients that have rented it.
        :return:
        """
        car_client_ids = {}  # dicts should have immutable objects as keys

        for rental in self._repo:
            if rental.car.id not in car_client_ids:
                car_client_ids[rental.car.id] = {rental.client.id}
            else:
                car_client_ids[rental.car.id].add(rental.client.id)

        result = []
        for car_id in car_client_ids:
            result.append(CarPopularityDTO(self.__car_repo.find(car_id), len(car_client_ids[car_id])))
        result.sort()
        return result
