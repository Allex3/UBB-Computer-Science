from lecture.livecoding.lecture_7.calc import add_calculator, create_calc, get_calc_value, undo_calculator

from lecture.livecoding.lecture_7.rational_as_list import create_rational, add_rational, to_str
# NOTE We import the same functions twice to show how Python handles the import statement.
# Generally speaking this is bad practice
from lecture.livecoding.lecture_7.rational_as_dict import create_rational, add_rational, to_str


# import lecture.livecoding.lecture_7.rational as r

def calculator_undo_ui(calculator):
    undo_calculator(calculator)


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
    options_dict = {"+": calculator_add_ui, "u": undo_calculator}
    calculator = create_calc()

    while True:
        print_menu()

        print("Value: " + to_str(get_calc_value(calculator)))
        print(type(get_calc_value(calculator)))
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
    # print(dir())
    start()

""""
command ui for calculator
    > add 1/3
    > add 1/9, 1/6, 56/67
    > undo
"""
