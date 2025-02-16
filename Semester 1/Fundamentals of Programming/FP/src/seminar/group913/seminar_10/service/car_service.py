from seminar.group913.seminar_10.repository.memory_repo import MemoryRepository
from seminar.group913.seminar_9.domain.car import Car


class CarService:
    def __init__(self, repo: MemoryRepository):
        self._repo = repo

    def get(self, car_id: int) -> Car:
        return self._repo[car_id]
