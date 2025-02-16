from seminar10.domain.rental import Rental
from datetime import date

class ValidatorException(Exception):
    def __init__(self, message_list="Validation error!"):
        self._message_list = message_list

    @property
    def messages(self):
        return self._message_list

    def __str__(self):
        result = ""
        for message in self.messages:
            result += message
            result += "\n"
        return result

class RentalValidator:
    def validate(self, rental):
        if isinstance(rental, Rental) is False:
            raise TypeError("Not a Rental")

        _errorList = []
        now = date(2024, 12, 3)
        if rental.start < now:
            _errorList.append("Rental starts in past;")
        if len(rental) < 5:
            _errorList.append("Rental must be at least 5 days;")
        if len(_errorList) > 0:
            raise ValidatorException(_errorList)