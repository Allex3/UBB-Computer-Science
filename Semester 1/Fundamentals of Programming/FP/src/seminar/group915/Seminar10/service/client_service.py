from seminar10.domain.client import Client
from seminar10.repository.memory_repo import MemoryRepository


class ClientService:
    def __init__(self, repo: MemoryRepository):
        self.__repo = repo

    def get(self, client_id: int) -> Client:
        return self.__repo[client_id]

    def get_all(self):
        return self.__repo