from seminar10.domain.rental import Rental
from seminar10.domain.rentalValidator import RentalValidator
from seminar10.repository.memory_repo import MemoryRepository
from seminar10.repository.text_repo import RentalRepository, CarTextFileRepository, ClientTextFileRepository
from seminar10.service.car_service import CarService
from datetime import date
from seminar10.domain.client import Client
from seminar10.domain.car import Car
from seminar10.service.client_service import ClientService


class CarRentalDaysDTO:
    # Data Transfer Object between service and UI layer
    def __init__(self, car, rental_days):
        self._car = car
        self._rental_days = rental_days

    @property
    def car(self):
        return self._car

    @property
    def days(self):
        return self._rental_days

    def __le__(self):
        # NOTE for sorting
        pass

    def __str__(self):
        return str(self.days) + " for car " + str(self.car)


class RentalService:
    # To do its job, the RentalService needs the rental repo, a car service
    # and a way to validate car instances
    def __init__(self, repo: RentalRepository, car_service: CarService, clientService: ClientService, validator: RentalValidator):
        self.__repo = repo
        self.__carService = car_service
        self.__clientService = clientService
        self.__validator = validator

    # We assume we read fields in the UI and create the object here
    def add(self, rental_id: int, start_date: date, end_date: date, client: Client, car: Car):
        # 1. Create the object
        rent = Rental(rental_id, start_date, end_date, client, car)
        # 2. Validate it -> exception if something is wrong
        self.__validator.validate(rent)
        # 3. Add to rentals repo
        self.__repo.add(rent)

    def statistic_cars_by_rental_days(self):
        # NOTE keys are car license plates, values are total rental days
        rental_dict = {}

        for rental in self.__repo:
            print(rental)
            if rental.car.id not in rental_dict:
                rental_dict[rental.car.id] = len(rental)
            else:
                rental_dict[rental.car.id] += len(rental)

        # TODO add all cars that were never rented
        result = []
        for key in rental_dict:
            car = self.__carService.get(key)
            result.append(CarRentalDaysDTO(car, rental_dict[key]))

        # sort by number of rental days
        result.sort(key=lambda x: x.days, reverse=True)
        return result

if __name__=="__main__":
    rentalRepository = RentalRepository()
    carRepo = CarTextFileRepository("cars.txt")
    carService = CarService(carRepo)
    clientRepo = ClientTextFileRepository("clients.txt")
    clientService = ClientService(clientRepo)
    rentalValidator = RentalValidator()
    rentalService = RentalService(rentalRepository, carService, clientService, rentalValidator)

    car = carService.get_all()[0]
    client = clientService.get_all()[0]

    #rental = Rental(98, date(2025, 1, 1), date(2025, 1, 10), client, car)

    rentalService.add(98, date(2022, 1, 1), date(2022, 1, 1), client, car)