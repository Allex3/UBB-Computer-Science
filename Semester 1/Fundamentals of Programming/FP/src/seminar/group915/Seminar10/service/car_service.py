from seminar10.repository.memory_repo import MemoryRepository
from seminar10.domain.car import Car


class CarService:
    def __init__(self, repo: MemoryRepository):
        self.__repo = repo

    def get(self, car_id: int) -> Car:
        return self.__repo[car_id]

    def get_all(self):
        return self.__repo