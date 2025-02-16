from lecture.livecoding.lecture_8.rational import Rational


class CalculatorError(Exception):
    pass


class Calculator:
    def __init__(self):
        """
        Create a calculator with a default value

        :return: The calculator initialized with the default value of 0
        """
        self.__value = Rational(0)
        self.__history = []
        # return {"value": create_rational(0), "history": []}

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        # append the old calculator value to the list
        self.__history.append(self.value)
        self.__value = new_value

    def add(self, q) -> None:
        """
        Add a rational number to the calculator

        :param calculator: The calculator's current state
        :param q: The number to add
        """
        # current_value = get_calc_value(calculator)
        # new_value = add_rational(current_value, q)
        self.value += q

    def undo(self) -> None:
        if len(self.__history) == 0:
            raise CalculatorError("Undo not available")
        last_value = self.__history.pop()
        # set_calc_value(calculator, last_value)
        self.__value = last_value
        # _set_calc_value_internal(calculator, last_value)
