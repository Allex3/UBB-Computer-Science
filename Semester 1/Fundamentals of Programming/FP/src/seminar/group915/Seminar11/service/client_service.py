from Seminar915.Seminar11.domain.client import Client
from Seminar915.Seminar11.service.undo_service import FunctionCall, Operation, CascadedOperation


class ClientService:
    def __init__(self, undo_service, rental_service, validator, repository):
        self._validator = validator
        self._repository = repository
        self._rental_service = rental_service
        self._undo_service = undo_service

    def create(self, client_id, client_cnp, client_name):
        client = Client(client_id, client_cnp, client_name)
        self._validator.validate(client)
        self._repository.store(client)

        functionRedo = FunctionCall(self._repository.store, client)
        functionUndo = FunctionCall(self._repository.delete, client_id)
        self._undo_service.recordUndo(Operation(functionUndo, functionRedo))

        return client

    def delete(self, client_id):
        """
            1. Delete the client
        """
        client = self._repository.delete(client_id)

        '''
            2. Delete their rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(client, None)
        for rent in rentals:
            self._rental_service.delete_rental(rent.id, False)

        functionRedo = FunctionCall(self._repository.delete, client_id)
        functionUndo = FunctionCall(self._repository.store, client)
        operations = [Operation(functionUndo, functionRedo)]

        rentalsRepo = self._rental_service.getRepo()
        for rental in rentals:
            functionRedo = FunctionCall(self._rental_service.delete_rental, rental.id)
            functionUndo = FunctionCall(rentalsRepo.store, rental)
            operations.append(Operation(functionUndo, functionRedo))

        self._undo_service.recordUndo(CascadedOperation(*operations))

        return client

    def get_client_count(self):
        return len(self._repository)

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        pass