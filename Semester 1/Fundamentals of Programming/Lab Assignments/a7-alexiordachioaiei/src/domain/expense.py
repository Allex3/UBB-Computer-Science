class Expense():
    def __init__(self, day: int, amount: int, type: str):
        self.day = day
        self.amount = amount
        self.type = type

    @property
    def day(self):
        return self.__day
    # day = property(day)

    @day.setter
    def day(self, value):
        if not (1<=value<=30):
            raise ValueError("Day should be between 1 and 30.")
        self.__day = value
    # day = day.setter(day), because day is not a property

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value: int):
        if value<=0:
            raise ValueError("Amount should be a positive integer.")
        self.__amount = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value: str|int):
        self.__type = str(value)

    def __str__(self):
        return f"Expense of type {self.__type} is due on day {str(self.__day)} for {str(self.__amount)}"

