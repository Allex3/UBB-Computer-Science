# My problems:
# From set A: 2
# From set B: 2
# Write the implementation for A5 in this file
#

# Console based app with a menu
"""
1 - Read a list of complex numbers
2 - Show list
3 - Display the largest subarray/subsequence with some PROPERTY
        a property from set A - naive implementation
        a property from set B - Dynamic Programming
        1, 2, 3 -> 1, 3 -> subsequence, 1, 2; 2, 3 -> subarrays
            subarrays are subsequences, but not the other way around
            indexes of elements have to be ordered in the subarray
4- Exit

Complex number, ex: 1+2i = [1, 2] -> [real, imaginary] parts
[[1, 2], [x, y], ...]
or [{1, 2}, {x, y}, ...] as a list of dictionaries!

List:
    Create complex number
    get_real
    get_imag
    set_real
    set_imag
    to_string

Dictionary:
    Create complex number
    get_real
    get_imag
    set_real
    set_imag
    to_string

THE PROGRAM SHOULD WORK FOR DICTIONARY OR FOR LIST REPRESENTATION THE SAME WAY
ONLY the above functiosn for lists and dictionary have to be different
Like if I comment out the dictionary list and uncomment the list ones
It should work, by ONLY doing that

MANDATORY functions to have beside the ones that work with the representation of complex numbers:
    - Read the complex number from console - UI
    - Display complex number to console - UI
    - Find ___ with property A - NON-UI
    - Find ___ with property B - NON-UI

    main loop (ofc) - UI

Separate the user interface from the rest of the program
(i.e. Do not print/read in an algorithm function, just do stuff in the background, not interacting with the user, NO CALLS to UI functions, just return)

NO global/non-local variables
NO nested functions -> function defined in function
"""
from random import randint
from venv import create

from numpy import number


#
# Write below this comment


# Functions to deal with complex numbers -- list representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#
# def create_complex_number(z: str) -> [int, int]:
#     """
#     Function to create complex number from string a+bi
#     :param z: The complex number a+bi as string
#     :return: The complex number data structure (dictionary)
#     """
#     z.strip()
#     negative_real_part = False
#     if z[0] == "-": #We have a real negative part, remember it's negative and get rid of this - in front
#         #So only the - or + between the real and imaginary part remains
#         negative_real_part = True
#         z = z[1:]
#
#     s = str()
#     if "+" in z:
#         s = z.split("+")
#     if "-" in z:
#         s = z.split("-")  # s = [a], [bi], two strings
#
#     try:
#         new_complex_number = [int(s[0]), int(s[1][:-1])]  # remove the "i" from the imaginary part string representation
#         if "-" in z: #imaginary part is negative
#             set_imag(new_complex_number, -get_imag(new_complex_number))  # if we have a -, the imaginary part is with a -
#         if negative_real_part: #negate the real part because it's negative
#             set_real(new_complex_number, -get_real(new_complex_number))
#     except ValueError:
#         raise ValueError("Your number isn't of value a+bi, a-bi, -a+bi or -a-bi")

#     return new_complex_number
#
#
# def get_real(z: [int, int]) -> int:
#     return z[0]
#
# def get_imag(z: [int, int]) -> int:
#     return z[1]
#
# def set_real(z: [int, int], re) -> None:
#     z[0] = re
#
# def set_imag(z: [int, int], i) -> None:
#     z[1] = i
#
# def to_string(z: [int, int]) -> str:
#     if get_imag(z) >= 0:
#         return f"{get_real(z)} + {get_imag(z)}i"
#     else:
#         return f"{get_real(z)} - {-get_imag(z)}i" #output in format a-bi, b is negative

#
# Write below this comment 
# Functions to deal with complex numbers -- dict representation
# -> There should be no print or input statements in this section 
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values
#

def create_complex_number(z: str) -> {int, int}:
    """
    Function to create complex number from string a+bi
    :param z: The complex number a+bi as string
    :return: The complex number data structure (dictionary)
    """
    z.strip()
    negative_real_part = False
    if z[0] == "-": #We have a real negative part, remember it's negative and get rid of this - in front
        #So only the - or + between the real and imaginary part remains
        negative_real_part = True
        z = z[1:]

    s = str()
    if "+" in z:
        s = z.split("+")
    if "-" in z:
        s = z.split("-")  # s = [a], [bi], two strings

    try:
        new_complex_number = {"re": int(s[0]), "imag": int(s[1][:-1])}  # remove the "i" from the imaginary part string representation
        if "-" in z: #imaginary part is negative
            set_imag(new_complex_number, -get_imag(new_complex_number))  # if we have a -, the imaginary part is with a -
        if negative_real_part: #negate the real part because it's negative
            set_real(new_complex_number, -get_real(new_complex_number))
    except ValueError:
        raise ValueError("Your number isn't of value a+bi, a-bi, -a+bi or -a-bi")

    return new_complex_number


def get_real(z: {int, int}) -> int:
    """
    Get the real part of a complex number
    :param z: The complex number
    :return: The real part of a complex number
    """
    return z["re"]


def get_imag(z: {int, int}) -> int:
    """
    Get the imaginary part of a complex number
    :param z: The complex number
    :return: The imaginary part of a complex number
    """
    return z["imag"]


def set_real(z: {int, int}, re: int) -> None:
    z["re"] = re


def set_imag(z: {int, int}, imag: int) -> None:
    z["imag"] = imag


def to_string(z: {int, int}) -> str:
    """
    Convert complex number to string
    :param z: The complex number
    :return: String representation of the complex number (a+bi)
    """
    if get_imag(z) >= 0:
        return f"{get_real(z)} + {get_imag(z)}i"
    else:
        return f"{get_real(z)} - {-get_imag(z)}i"  # output in format a-bi, b is negative


#
# Write below this comment
# Functions that deal with subarray/subsequence properties
# -> There should be no print or input statements in this section
# -> Each function should do one thing only
# -> Functions communicate using input parameters and their return values


def generate_random_list(n: int) -> list:
    number_list = []
    for _ in range(n):
        re = randint(-10, 10)
        imag = randint(-10, 10)
        z = str()
        if imag < 0:
            z = create_complex_number(f"{re}-{-imag}i")
        else:
            z = create_complex_number(f"{re}+{imag}i")
        number_list.append(z)

    return number_list


def get_modulus(z) -> float:
    re = get_real(z)
    imag = get_imag(z)
    return re * re + imag * imag  # it's in sqrt(), but easier to compare without it


def longest_subarray_of_same_modulus(number_list):  # A.2
    """
    The function returns one of the longest subarray of numbers having the same modulus.
    :param number_list:
    :return: The longest subarray of elements with the same modulus
    """

    # Since a subarray is composed of consecutive elements
    # We just check for each consecutive element if it has the same modulus as the last one
    # And keep incrementing the count of numbers in the subarray as long as they have the same modulus
    # If we reach a new maximum count, change the starting and ending index of the subarray
    start_index, end_index = 0, 0
    maximum_length = 0
    current_length = 1  # start with element number_list[0]
    last_modulus = get_modulus(number_list[0])  # modulus of the first number in the list
    for i in range(1, len(number_list)):  # 1 to n-1
        current_modulus = get_modulus(number_list[i])
        if (current_modulus == last_modulus):  # same modulus as the last number, add the element to subarray
            current_length += 1
        else:
            current_length = 1  # reset the subarray, no more equal consecutive modulus'

        if current_length > maximum_length:  # new maximum length, create a new subarray solution
            maximum_length = current_length
            start_index = i - maximum_length + 1  # the maximum_length elements are from i-maximum_length+1, +2, ..+maximum_length=i
            # this is the subarray that has maximum_length number of elements and stops at i
            end_index = i

        last_modulus = current_modulus

    return number_list[start_index:end_index + 1]


def binary_search_p(D: list[int], x: int, k: int) -> int:
    """
    Returns the position of the smallest element in D, higher than the number
    :param D: List of numbers
    :param x: Number for which to find that position
    :param k: number of elements in D
    :return: Position in D
    """

    left, right = 1, k
    p = 0
    while left <= right:
        mid = (left + right) // 2
        if D[mid] >= x:
            right = mid - 1
            p = mid  # save current position, this may be the smallest element higher than the number
            # if it isn't, go to the left and look for another higher one but smaller
        else:
            left = mid + 1

    return p


def get_longest_increasing_subsequence(number_list: list) -> list:
    """
    Function to compute the longest increasing subsequence of a list of integers
    :param number_list: The number list
    :return: The longest increasing subsequence of number_list
    """
    D = [0 for _ in range(len(number_list) + 1)]
    k = 1
    D[k] = get_real(number_list[0])  # D[j] -> last element of an increasing subsequence of length j
    # Since subsequences don't have to be composed of consecutive elements:
    # Iterate through the number list and if number_list[i] >= D[k] then
    # We have a new maximal increasing subsequence
    # (D[k] is the last element an increasing subsequence of length k
    # So all the elements are increasing, and adding number_list[i] to that, which is bigger
    # Forms a new, longer increasing subsequence, and that is D[k+1]
    # The length k is incremented by 1 and the last element of it is number_list[i]

    # But, if number_list[i] < D[k], then we cannot form a bigger subsequence with it
    # But what we will do, we replace the smallest element in D, that is bigger than number_list[i],
    # with number_list[i], and we do that in O(log(n)), because D is increasing
    # Since the only numbers we add, when we increment K, are numbers bigger than D[k]
    # So we can use binary search for it

    # At the end, k is the length of a maximal increasing subsequence
    # To print that subsequence, we add a new list position, which position[i] represents the position
    # of number_list[i], the element at index i in number_list, but in the list D
    # Then we iterate through D, and for each i from k to 1, we search for a position[j] which is i
    # j starts from n, and it goes to the left
    # After we find a position[j], put it in the solution list, it is part of the solution, but in reverse order
    # Then continue to the left of this j, finding an element which has the position i-1 in the D vector
    # That, by the algorithm, is smaller than the element after it, successfully computing the subsequence

    position = [0 for _ in range(len(number_list))]
    for i in range(1, len(number_list)):
        if (get_real(number_list[i]) >= D[k]):
            k += 1
            D[k] = get_real(number_list[i])
            position[i] = k  # number_list[i] is at position k right now in the vector D
        else:
            pos = binary_search_p(D, get_real(number_list[i]), k)
            D[pos] = get_real(number_list[i])
            position[i] = pos  # number_list[i] is at position p right now in vector D

    solution = []
    j = len(number_list) - 1
    for i in range(k, 0, -1):  # go from k to 1 to reconstruct the solution
        while (position[j] != i and j > 0):
            j -= 1
        # we got to a number at position j in number_list whose position is i in D
        solution.append(number_list[j])

    solution.reverse()
    return solution


#
# Write below this comment 
# UI section
# Write all functions that have input or print statements here
# Ideally, this section should not contain any calculations relevant to program functionalities

def read_complex_number():
    """
    Function to read a complex number from the console
    :return: The complex number data structure
    """

    z = input("Input the complex number (a+bi or a-bi): ")
    return create_complex_number(z)


def read_number_list(n: int) -> list:
    number_list = []
    for _ in range(n):
        number_list.append(read_complex_number())

    return number_list


def write_complex_number(z) -> None:
    print(to_string(z))


def display_number_list(number_list: list) -> None:
    n = len(number_list)
    for i in range(n-1):
        print(to_string(number_list[i]), end=", ")
    print(to_string(number_list[n - 1]))


def print_menu() -> None:
    print("Menu options")
    print("1. Read a list of complex numbers")
    print("2. Display the list of complex numbers")
    print("3. Display a longest subarray of numbers having the same modulus.")
    print("4. Display a longest increasing subsequence, when considering each number's real part.")
    print("0. Exit")


def menu() -> None:
    """
    Function to display the menu and run it until the user exits the program
    :return: None
    """
    number_list = generate_random_list(10)  # list of complex numbers to be read
    display_number_list(number_list)
    while (True):
        print_menu()
        option = int(input(">>> "))
        if option == 1:
            try:
                n = int(input("How many numbers do you want in the list: "))
                number_list = read_number_list(n)
            except ValueError:
                print("Your value is not an integer.")
        elif option == 2:
            if not number_list:
                print("The list of complex numbers is empty.")
                continue
            display_number_list(number_list)
        elif option == 3:
            if not number_list:
                print("The list of complex numbers is empty.")
                continue
            longest_subarray = longest_subarray_of_same_modulus(number_list)
            print("The longest subarray of numbers having the same modulus is :")
            display_number_list(longest_subarray)
            print(f"It has the length of {len(longest_subarray)}")


        elif option == 4:
            if not number_list:
                print("The list of complex numbers is empty.")
                continue
            longest_increasing_subsequence = get_longest_increasing_subsequence(number_list)
            print("The longest increasing subsequence when considering the real parts of the numbers is: ")
            display_number_list(longest_increasing_subsequence)
            print(f"It has the length of {len(longest_increasing_subsequence)}")
        elif option == 0:
            return  # Exit the program
        else:
            """
            catches everything that is not in the list (not 1-4)
            """
            print("Bad command")
            continue


if __name__ == "__main__":
    menu()
