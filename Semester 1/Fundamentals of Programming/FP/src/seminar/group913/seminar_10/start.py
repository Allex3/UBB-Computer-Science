from datetime import date, timedelta

from faker.proxy import Faker

from seminar.group913.seminar_10.domain.client import Client
from seminar.group913.seminar_10.domain.rental import Rental
from seminar.group913.seminar_10.repository.memory_repo import MemoryRepository
from seminar.group913.seminar_10.repository.text_repo import RentalTextFileRepository
from seminar.group913.seminar_10.service.rental_service import RentalService
from seminar.group913.seminar_9.domain.car import Car

from random import choice, randint


def generate_cars():
    car_list = []
    car_list.append(Car(100, "CJ 01 YUI", "Audi A3"))
    car_list.append(Car(101, "SJ 56 RGV", "Toyota Hilux"))
    car_list.append(Car(102, "B 567 QWN", "Dacia Jogger"))
    car_list.append(Car(103, "VS 66 PLO", "Suzuki Vitara"))
    car_list.append(Car(104, "CT 45 CFT", "VW T-Roc"))
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
        start_date = date(2024, randint(1, 12), randint(1, 30))
        rental_days = timedelta(days=randint(1, 10))
        rental_list.append(
            Rental(rental_id, start_date, start_date + rental_days, choice(client_list), choice(car_list)))

    return rental_list


if __name__ == "__main__":
    # rentals = generate_rentals(generate_cars(), generate_clients())
    car_repo = MemoryRepository()
    for car in generate_cars():
        car_repo.add(car)

    client_repo = MemoryRepository()
    for client in generate_clients():
        client_repo.add(client)

    rental_text_repo = RentalTextFileRepository(car_repo, client_repo)
    # for r in rental_text_repo:
    # rental_text_repo.add(r)
    # print(r)

    rental_service = RentalService(rental_text_repo, car_repo)
    result = rental_service.most_popular_cars()

    for data in result:
        print(str(data.car) + " was rented by " + str(data.clients) + " different clients")
