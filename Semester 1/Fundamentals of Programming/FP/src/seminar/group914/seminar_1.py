"""
FP seminar 1 problems & solutions

How to set up things!
    1. An installation of Python 3
    2. An IDE --> PyCharm
    3. A GitHub account -- needed to accept assignments
"""

# print("Hello World!")

"""
Process finished with exit code 0
    - you need to see this to make sure the program has stopped :)
    - exit code 0 means no errors 
"""

"""
Problem statements to choose from:
    https://www.codecademy.com/resources/blog/python-code-challenges-for-beginners/
    https://www.freecodecamp.org/news/python-coding-challenges-for-beginners/
"""

"""
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
Question – What happens if we enter a non-integer number, or alphanumeric characters?
"""

"""
    static = at compile time
    dynamic = at run time
    
    strongly typed language = at every moment, every variable has a well known type 
"""

# Python is a dynamically typed language
# a = "abcd"
# a = 2345

# a = input("First value =")  # input returns a string (Python's str type)
# b = input("Second value =")

"""
The function below uses Python type hints
    a : int (means that the type of parameter a should be int)
    -> bool (means that the functions should return a value of type bool)
"""


def is_sum_10(a: int, b: int) -> bool:
    if a == 10 or b == 10 or a + b == 10:
        return True
    else:
        return False


# a = int(input("First value ="))  # int() is a Python builtin function to convert an str to an int
# b = int(input("Second value ="))
# is_sum_10(a, b)

# print(a + b)  # if a and b are str, + is concatenation
# if a and b are numbers, + is addition

"""
2. Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
"""

# V1 - without functions
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# V2 - turn this into a function
def fizz_buzz(left: int, right: int) -> list:
    result = []  # empty list in Python
    for i in range(left, right + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result


print(fizz_buzz(1, 10))

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
