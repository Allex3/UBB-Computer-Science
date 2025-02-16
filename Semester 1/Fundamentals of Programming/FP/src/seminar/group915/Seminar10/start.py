from datetime import date, timedelta

from faker.proxy import Faker

from seminar10.domain.client import Client
from seminar10.domain.rental import Rental
from seminar10.domain.car import Car

from random import choice, randint

from seminar10.domain.rentalValidator import RentalValidator, ValidatorException
from seminar10.repository.text_repo import CarTextFileRepository, ClientTextFileRepository, RentalRepository
from seminar10.service.car_service import CarService
from seminar10.service.rental_service import RentalService
from seminar10.service.client_service import ClientService


def generate_cars():
    car_list = []
    car_list.append(Car(100, "CJ 01 YUI", "Audi", "A3", "White"))
    car_list.append(Car(101, "SJ 56 RGV", "Toyota", "Hilux", "Black"))
    car_list.append(Car(102, "B 567 QWN", "Dacia", "Jogger", "Gray"))
    car_list.append(Car(103, "VS 66 PLO", "Suzuki", "Vitara", "Red"))
    car_list.append(Car(104, "CT 45 CFT", "VW", "T-Rock", "Green"))
    return car_list


def generate_clients():
    client_list = []
    fake = Faker()

    for client_id in range(200, 205):
        client_list.append(Client(client_id, fake.name()))
    return client_list


def generate_rentals(car_list: [Car], client_list: [Client]):
    rental_list = []
    for rental_id in range(300, 320):
        start_date = date(2025, randint(1, 12), randint(1, 28))
        rental_days = timedelta(days=randint(1, 10))
        carIndex = randint(0, len(car_list) - 1)
        clientIndex = randint(0, len(client_list) - 1)
        rental_list.append(Rental(rental_id, start_date, start_date + rental_days, client_list[clientIndex], car_list[carIndex]))

    return rental_list

if __name__ == "__main__":
    #for r in generate_rentals(generate_cars(), generate_clients()):
    #    print(r)
    """
    repo = CarTextFileRepository("cars.txt")
    car = Car(99, "BN 99 USB", "Dacia", "Sandero", "pink")
    repo.add(car)
    repo = ClientTextFileRepository("clients.txt")
    for client in repo:
        print(client)
    """
    car_repo = CarTextFileRepository("cars.txt")
    clientRepo = ClientTextFileRepository("clients.txt")
    rental_repo = RentalRepository()

    # NOTE You can switch the repo and validator you use without changing
    # the service class source code
    # NOTE this is named "dependency injection"
    car_service = CarService(car_repo)
    clientService = ClientService(clientRepo)

    rentalValidator = RentalValidator()

    rental_service = RentalService(rental_repo, car_service, clientService, rentalValidator)

    valid_client_list = [client for client in clientService.get_all() if client is not None]
    valid_car_list = [car for car in car_service.get_all() if car is not None]
    rentals = generate_rentals(valid_car_list, valid_client_list)

    try:
        for r in rentals:
            rental_service.add(r.id, r.start, r.end, r.client, r.car)
    except ValidatorException as e:
        print(e)

    try:
        rental_service.add(99999, date(2025, 1, 1), date(2025, 1, 1), valid_client_list[0], valid_car_list[0])
    except ValidatorException as e:
        print(e)

    statistic_result = rental_service.statistic_cars_by_rental_days()
    for sr in statistic_result:
        print(sr)

    # for s in statistic_result:
    #     print(s)

    # ui = UI( < pass all services here >)
    # ui.start()

    # for car in generate_cars(20):
    #     car_repo.add(car)
