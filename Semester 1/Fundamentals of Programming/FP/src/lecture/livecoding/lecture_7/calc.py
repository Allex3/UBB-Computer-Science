from lecture.livecoding.lecture_7.rational_as_list import create_rational, add_rational
# NOTE We import the same functions twice to show how Python handles the import statement.
# Generally speaking this is bad practice
from lecture.livecoding.lecture_7.rational_as_dict import create_rational, add_rational


def create_calc():
    """
    Create a calculator with a default value

    :return: The calculator initialized with the default value of 0
    """
    return {"value": create_rational(0), "history": []}


def get_calc_value(calculator):
    return calculator["value"]


def _set_calc_value_internal(calculator, q):
    # set the new calculator value
    calculator["value"] = q


def set_calc_value(calculator, q):
    # append the old calculator value to the list
    calculator["history"].append(calculator["value"])
    _set_calc_value_internal(calculator, q)


def add_calculator(calculator, q) -> None:
    """
    Add a rational number to the calculator

    :param calculator: The calculator's current state
    :param q: The number to add
    """
    current_value = get_calc_value(calculator)
    new_value = add_rational(current_value, q)
    set_calc_value(calculator, new_value)


def undo_calculator(calculator) -> None:
    if len(calculator["history"]) == 0:
        # NOTE ValueError is perhaps not fitting here but we don't know other exceptions ... yet :(
        raise ValueError("Undo not available")
    last_value = calculator["history"].pop()
    # set_calc_value(calculator, last_value)
    _set_calc_value_internal(calculator, last_value)
