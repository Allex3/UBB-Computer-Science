"""
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
Question – What happens if we enter a non-integer number, or alphanumeric characters?
"""

def solveProblem1(a, b):
    """
    Function that checks if either a, b or their sum is 10.
    :param a: integer
    :param b: integer
    :return: a boolean: True if a, b or a + b is 10
                        False otherwise
    """
    if type(a) != int or type(b) != int:
        return False

    returnValue = False

    if a == 10 or b == 10 or a + b == 10:
        returnValue = True

    return returnValue


def solveProblem11(a, b):
    return a == 10 or b == 10 or a + b == 10

def firstTypeOfDefiningAFunction():
    firstVarialeNaming = 0
    return firstVarialeNaming

def second_type_of_defining_a_function():
    second_variable_naming = 0
    return second_variable_naming

"""
2. Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
"""

def FizzBuzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

"""
3. Calculate the first n terms of the Fibonacci sequence
"""

def computeNFibonacciTerms(n):
    if n <= 0:
        return 0

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    fibonacciSequence = [0, 1]
    for i in range(2, n):
        fibonacciTerm = fibonacciSequence[-1] + fibonacciSequence[-2]
        fibonacciSequence.append(fibonacciTerm)

    return fibonacciSequence

"""
4. Write a Python program to calculate body mass index.
   BMI = weight / (height * height)
   How do we validate the code above for user input?
   Let's write the specification for it
"""

def computeBodyMassIndex(weight, height):
    """
    Function that computes the body mass index.
    :param weight: strictly positive float, should be in kg
    :param height: strictly positive float, should be in meters
    :return: BMI, a strictly positive float
    """

    return weight / (height * height)


"""
7. Return the sum of the numbers in a list, returning 0 for an empty list. Except the number 13 is very 
unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""

def computeLuckySum(initialList):
    if len(initialList) == 0:
        return 0

    sum  = 0
    for i in range(len(initialList)):
        if i != 0 and initialList[i] != 13 and initialList[i - 1] != 13:
            sum += initialList[i]
        if i == 0 and initialList[i] != 13:
            sum += initialList[i]

    return sum


def main():
    '''
    a = 3
    b = 4

    print(type(a))

    if type(a) == type(b):
        print("Here here")

    if id(a) == id(b):
        print("Are they the same?")

    print(id(a))
    if type(a) == int:
        print("This is an integer")
    a = "abc"
    print(type(a))
    '''

    """
    print(solveProblem1(10, 4))
    print(solveProblem1(6, 4))
    print(solveProblem1(5, 3))
    print(solveProblem1("abc", 3))
    """

    #FizzBuzz()

    """
    try:
        n = int(input("Number of Fibonacci terms: "))
        print(computeNFibonacciTerms(n))
    except ValueError:
        print("Please give us a valid integer value")
    """

    #print(round(computeBodyMassIndex(85.0, 1.90), 2))

    try:
        n = int(input("Number of Fibonacci terms: "))
        luckyList = []
        for i in range(n):
            elem = int(input("Element = "))
            luckyList.append(elem)

        print(computeLuckySum(luckyList))
    except ValueError:
        print("Please give us a valid integer value")

main()


