from seminar.group913.seminar_11.domain.car import Car
from seminar.group913.seminar_11.service.undo_service import FunctionCall, Operation, CascadedOperation


class CarService:
    def __init__(self, undo_service, rental_service, validator, repository):
        self._validator = validator
        self._repository = repository
        self._rental_service = rental_service
        self._undo_service = undo_service

    def create(self, car_id, license_plate, car_make, car_model):
        car = Car(car_id, license_plate, car_make, car_model)
        self._validator.validate(car)
        self._repository.store(car)
        return car

    def delete(self, car_id):
        """
            1. Delete the car from the repository
        """
        car = self._repository.delete(car_id)

        """
            2. Record how to undo/redo the operation
        """
        # NOTE Only record successfully completed operations
        # Version 1 -- does not take the car's rentals into account
        # undo_function = FunctionCall(self._repository.store, car)
        # redo_function = FunctionCall(self._repository.delete, car_id)
        # self._undo_service.record(Operation(undo_function, redo_function))

        # Version 2 -- also considers existing rentals when undo/redo
        undo_redo_operation = CascadedOperation()
        undo_redo_operation.add_undo_function(FunctionCall(self._repository.store, car))
        undo_redo_operation.add_redo_function(FunctionCall(self._repository.delete, car_id))

        '''
            2. Delete its rentals
            NB! This implementation is not transactional, i.e. the two delete operations are performed separately
        '''
        rentals = self._rental_service.filter_rentals(None, car)
        for rent in rentals:
            self._rental_service.delete_rental(rent.id)

            # Also record rentals for undo/redo
            undo_redo_operation.add_undo_function(
                FunctionCall(self._rental_service.create_rental, rent.id, rent.client, rent.car, rent.start, rent.end))
            undo_redo_operation.add_redo_function(FunctionCall(self._rental_service.delete_rental, rent.id))

        self._undo_service.record(undo_redo_operation)
        return car

    def update(self, car):
        """
            NB! Undo/redo is also needed here
        """
        # TODO Implement later...
        pass
