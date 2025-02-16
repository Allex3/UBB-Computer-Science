"""
FP seminar 1 problems & solutions
"""

"""
What you will need:
    1. An installation of Python 3              (the Python interpreter)
    2. The PyCharm IDE (Community or Ultimate)  (the development environment, debug, code suggestion, auto-complete, running tests, code coverage)
    3. A GitHub account                         (accept and work on the lab assignments, use as a portofolio)
"""
# print("Hello World!")  # print is a builtin function

# int a = 1024;
# a = "abcd" -> compile error

"""
    C/C++ are statically typed -> the exact type of each variable is set and known at compile time
    Python is dynamically typed -> the exact type of each variable is known only at runtime
    
    In Python:
    a = 1234
        
        1. The type of variable a is transferred from the type of 1234 (int)
        2. The value  of variable a is transferred from the type of 1234 (int)
"""

# a = 1024  # a is a variable of type int holding the value 1024
# a = "abcd"  # the type of a now becomes str and its value is "abcd"

"""
Problem statements to choose from:
    https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
    https://www.freecodecamp.org/news/python-coding-challenges-for-beginners/
"""

"""
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
Question – What happens if we enter a non-integer number, or alphanumeric characters?
"""


def is_ten(a: int, b: int) -> bool:
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


# a = int(input("First value ="))  # input is a builtin function that reads from the console and returns an str
# b = int(input("second value ="))  # int()  is a builtin function that converts its parameter to the int type
# print(is_ten(a, b))

# print(a + b)  # if a and b are str, then + is concatenation

"""
2. Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
"""


def fizz_buzz(left: int, right: int) -> list:
    result = []  # [] is an empty list

    for i in range(left, right + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
            # print("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


# values = fizz_buzz(1, 50)
# print(values)

"""
3. Calculate the first n terms of the Fibonacci sequence
"""

"""
4. Write a Python program to calculate body mass index.
   How do we validate the code above for user input?
   Let's write the specification for it
"""

"""
4. Given a non-empty string like "Code" return a string like "CCoCodCode"
    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
"""


def string_splosion(s: str) -> str:
    result = ""

    for index in range(1, len(s) + 1):
        result += s[0:index]  # str is a sequence type and immutable
        # += operator creates a new str each time

        print(type(result))  # type() is a builtin function
        print(id(result))  # id() provides the unique id of a variable

    return result


print(string_splosion('Code'))

# s = 'Code'  # str is a seuqence type
# print(s[1:3])

"""
5. Given 2 strings, a and b, return the number of the positions where they contain the same length 2
substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the
same place in both strings.
    stringMatch('xxcaazz', 'xxbaaz') → 3
    stringMatch('abc','abc) → 2
        stringMatch('abc', 'axc') → 0
"""

"""
6. Write a Python program to remove all duplicate elements from a given array and returns a new array.
"""

"""
7. Return the sum of the numbers in a list, returning 0 for an empty list. Except the number 13 is very
unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""

"""
8. Caesar Encryption
"""
