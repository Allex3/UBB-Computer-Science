from seminar.group914.seminar_10.domain.rental import Rental
from seminar.group914.seminar_10.repository.memory_repo import MemoryRepository


class RentalService:
    def __init__(self, repo: MemoryRepository):
        self._repo = repo

    def get(self, rental_id: int) -> Rental:
        return self._repo[rental_id]
