from multiprocessing.managers import Value


class Rational(object):
    # class Rational is derived from class object
    # object - the root of Python's class hierarchy

    __number_of_objects = 0

    """
    class = data type = state + operations
        class state = the class fiels
        class operations = class methods
    """

    def __init__(self, num: int, denom: int = 1):
        # self.numerator is "public" -> accessible from everywhere
        # self.numerator = num
        # self.denominator = denom

        # self._numerator is "protected" -> accessible from within the class or derived classes
        # "protected" is a convention
        # self._numerator = num
        # self._denominator = denom

        if denom == 0:
            raise ValueError("Denominator must be !=0")

        # self.__numerator is "private" -> accessible from within the class
        self.__numerator = num
        self.__denominator = denom
        Rational.__number_of_objects += 1

    def get_numerator(self) -> int:
        return self.__numerator

    def set_numerator(self, new_value: int):
        self.__numerator = new_value

    def get_denominator(self) -> int:
        return self.__denominator

    def set_denominator(self, new_value: int):
        if new_value == 0:
            raise ValueError("Denominator must be !=0")
        self.__denominator = new_value

    @property
    def numerator(self):
        return self.__numerator

    @numerator.setter
    def numerator(self, new_value: int):
        self.set_numerator(new_value)

    @property
    def denominator(self):
        return self.__denominator

    @denominator.setter
    def denominator(self, new_value: int):
        self.set_denominator(new_value)

    @staticmethod
    def get_number_of_objects():
        return Rational.__number_of_objects

    def __add__(self, other):
        num = self.numerator * other.denominator + self.denominator * other.numerator
        den = self.denominator * other.denominator
        return Rational(num, den)

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return str(self.numerator) + "/" + str(self.denominator)


if __name__ == "__main__":
    try:
        q = Rational(1, 0)
    except ValueError as ve:
        print(ve)

    q = Rational(1, 3)

    # option 1
    q.get_numerator()

    # option 2
    Rational.get_numerator(q)
    """
    What to learn from these options?
        The computer's memory stores a copy of each set of class fields for each object
            1000 rational numbers => 1000 numerators, 1000 denominators
            1000 rational numbers => a single copy of each method, including __init__ :)
        
    
    """

    # print(q.get_numerator(),q.get_denominator())
    # q.set_denominator(0)

    q = Rational(3, 4)

    q2 = q + Rational(1, 4) + q + q
    print(q2)
    print("How many Rational objects? = ", Rational.get_number_of_objects())

    # q.set_numerator(q.get_numerator() + 1)  # increase by 1

    q2.numerator += 5
    # print(q.numerator)
    # q.numerator = 99
    # q.numerator += 1
    # print(q)  # print(...) prints out an str, so the str() builtin is called implicitly
    # q.denominator -= 4

    # print(q.numerator)

    # q = Rational(3, 4)
    # print(q)
    # print(type(q))
    # print(q.numerator, q.denominator)
    # q.denominator = 0
    # q.numerator = "abc"
    # print(q.__numerator, q.__denominator)
