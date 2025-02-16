from seminar10.domain.client import Client
from seminar10.repository.memory_repo import MemoryRepository


class ClientService:
    def __init__(self, repo: MemoryRepository):
        self._repo = repo

    def get(self, client_id: int) -> Client:
        return self._repo[client_id]

    def getAll(self):
        return self._repo