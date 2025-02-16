"""

Create a calculator program for rational numbers with the following functionalities:
    + add a rational number to the calculator
    u undo the last operation
    x exit
"""

from math import gcd


# ----------------------#
# Non-UI functions here #
# ----------------------#

# Functions to handle rational numbers

def create_rational(num: int, denom: int = 1):
    """
    Create a rational number
    :param num: numerator
    :param denom: non-zero denominator
    :return: the created number

    :raises: Raises ValueError in case the denom is 0
    """
    if denom == 0:
        raise ValueError("Denominator must be non-0")

    _gcd = gcd(num, denom)
    return {"num": num // _gcd, "denom": denom // _gcd}


def get_numerator(q) -> int:
    return q["num"]


def get_denominator(q) -> int:
    return q["denom"]


def to_str(q) -> str:
    # TODO fix 1/-2, 5/-1 etc.
    if get_denominator(q) == 1:
        return str(get_numerator(q))
    return str(get_numerator(q)) + "/" + str(get_denominator(q))


def add_rational(q1, q2):
    gn = get_numerator  # () -- function call operator
    gd = get_denominator
    num = gn(q1) * gd(q2) + gn(q2) * gd(q1)
    denom = gd(q1) * gd(q2)
    return create_rational(num, denom)


"""
    1. Test functions don't take parameters and return nothing :( 
    2. Test functions can be run in amy order
    3. Test functions do not interact with the user
    4. Test function executions don't produce an effect as long as the test passes
    5. Test functions result in an AssertionError in case of problems 
"""


def test_rational():
    q = create_rational(10, 2)
    assert get_numerator(q) == 5
    assert get_denominator(q) == 1

    q = create_rational(2, 3)
    assert get_numerator(q) == 2
    assert get_denominator(q) == 3
    """
    Syntax:
    assert <condition>
    if <condition> == True, nothing happens => test has passed
    if <condition> == False, AssertionError is raised => test has failed :(
    """

    q = create_rational(47, 1)
    assert get_numerator(q) == 47
    assert get_denominator(q) == 1

    q = create_rational(23)
    assert get_numerator(q) == 23
    assert get_denominator(q) == 1

    q = create_rational(0)
    assert get_numerator(q) == 0
    assert get_denominator(q) == 1

    try:
        q = create_rational(5, 0)
        assert False  # the function above should have raised a ValueError
    except ValueError:
        assert True

    q1 = create_rational(2, 3)
    q2 = create_rational(2, 3)
    q3 = add_rational(q1, q2)  # 4/3
    assert get_numerator(q3) == 4
    assert get_denominator(q3) == 3

    q1 = create_rational(6, 3)
    q2 = create_rational(6, 3)
    q3 = add_rational(q1, q2)  # 12/3 == 4
    assert get_numerator(q3) == 4
    assert get_denominator(q3) == 1


"""
    A few problems with this implementation :(
    1. We have to explicitly call test functions
    2. Separate running the tests from running the program
    3. Keep running existing tests, even when some of them fail
    4. How do I know I've written enough tests?
    5. A fancier way of examining test results :)
"""
test_rational()


# Functions to handle the calculator

def create_calc():
    """
    Create a calculator with a default value

    :return: The calculator initialized with the default value of 0
    """
    return {"value": create_rational(0)}


def get_calc_value(calculator):
    return calculator["value"]


def set_calc_value(calculator, q):
    calculator["value"] = q


def add_calculator(calculator, q) -> None:
    """
    Add a rational number to the calculator

    :param calculator: The calculator's current state
    :param q: The number to add
    """
    current_value = get_calc_value(calculator)
    new_value = add_rational(current_value, q)
    set_calc_value(calculator, new_value)


def test_calculator():
    calc = create_calc()
    val = get_calc_value(calc)
    assert get_numerator(val) == 0
    assert get_denominator(val) == 1

    add_calculator(calc, create_rational(1, 4))
    val = get_calc_value(calc)
    assert get_numerator(val) == 1
    assert get_denominator(val) == 4

    add_calculator(calc, create_rational(3, 4))
    val = get_calc_value(calc)
    assert get_numerator(val) == 1
    assert get_denominator(val) == 1


test_calculator()


# -----------------------#
# Only UI functions here #
# -----------------------#


def calculator_add_ui(calculator):
    try:
        numerator = int(input("numerator="))
        denominator = int(input("denominator="))
    except ValueError:
        raise ValueError("Numerator/denominator must be integers")
    add_calculator(calculator, create_rational(numerator, denominator))


def print_menu():
    print("Calculator menu:")
    print("   + add a rational number")
    print("   u undo last operation")
    print("   x close the calculator")


def start():
    options_dict = {"+": calculator_add_ui}
    calculator = create_calc()

    while True:
        print_menu()

        print("Value: " + to_str(get_calc_value(calculator)))
        option = input(">")
        if option in options_dict:
            try:
                options_dict[option](calculator)
                # "+" -> calculator_add_ui(calculator)
            except ValueError as ve:
                print(ve)
        elif option == "x":
            return
        else:
            print("Invalid command")


if __name__ == "__main__":
    start()
