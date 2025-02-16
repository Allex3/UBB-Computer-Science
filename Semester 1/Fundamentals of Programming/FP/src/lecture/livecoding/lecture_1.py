"""
Problem statement:
    1. Read a string from the program's console
    2. Divide the string into numbers, words (using space)
    3. Build a list of primes, a list of negative numbers, a list of the rest of the numbers, a list
    of capitalized names

    4. Print out all primes numbers etc. in ascending order, without duplicates :)
"""
from math import sqrt


def is_capitalized(word: str) -> bool:
    return 'A' <= word[0] <= 'Z'


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    # range -> start with 3 then +2 at every step until sqrt(n) + 1
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def process_list(data: list) -> list:
    # set() creates a mathematical set with the elements of the list supplied as a parameter, which will eliminate duplicates
    # list() creates a list with the elements of the set supplied as a parameter. Lists are sortable :)
    # NOTE There is probably a better way to carry out this transformation
    data = list(set(data))
    data.sort()
    return data


def start():
    """
    NOTE you can use the following input to test the program:
    45 -14 23 -5 Anna has apples 55 -50 23 -5 James 47 999
    """
    tokens = input("Give the string =").split(" ")

    primes_list = []  # empty list
    negatives_list = []
    other_numbers_list = []
    cap_names_list = []

    for token in tokens:
        try:
            int_token = int(token)  # int() is a builtin function to convert to integer
            # if there's an error on the previous line, the execution skips directly
            # to the except clause below
            if int_token < 0:
                negatives_list.append(int_token)
            elif is_prime(int_token):
                primes_list.append(int_token)
            else:
                other_numbers_list.append(int_token)
        except ValueError:
            if is_capitalized(token):
                cap_names_list.append(token)

    print("Prime numbers: ", process_list(primes_list))
    print("Negative numbers: ", process_list(negatives_list))
    print("Other numbers: ", process_list(other_numbers_list))
    print("Capitalized names: ", process_list(cap_names_list))


start()
