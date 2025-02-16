from seminar10.repository.memory_repo import MemoryRepository
from seminar10.domain.car import Car


class CarService:
    def __init__(self, repo: MemoryRepository):
        self._repo = repo

    def get(self, car_id: int) -> Car:
        return self._repo[car_id]

    def getAll(self):
        return self._repo