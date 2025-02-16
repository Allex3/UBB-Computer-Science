"""
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
Question – What happens if we enter a non-integer number, or alphanumeric characters?
"""

def solveProblem1(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError("A and B should be integers")

    return  a == 10 or b == 10 or a + b == 10

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
        return 0

    if n == 2:
        return [0, 1]

    fibonacciSequence = [0, 1]
    for i in range(2, n):
        newFibonacciTerm = fibonacciSequence[-1] + fibonacciSequence[-2]
        fibonacciSequence.append(newFibonacciTerm)

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
    :return: BMI(body mass index) - float
    """
    return weight / (height * height)

"""
7. Return the sum of the numbers in a list, returning 0 for an empty list. Except the number 13 is very 
unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
"""

def computeLuckySum(luckyList):
    """
    Function that computes the sum of the elements from a list, except elements equal to 13 or elements that come immediately after a 13.
    :param luckyList: a list of integers
    :return: sum - integer
    """
    if len(luckyList) == 0:
        return 0

    sum = 0
    for i in range(len(luckyList)):
        if i > 0 and luckyList[i] != 13 and luckyList[i - 1] != 13:
            sum += luckyList[i]
        elif i == 0 and luckyList[i] != 13:
            sum += luckyList[i]

    return sum



def main():
    """
    a = 7
    b = 9

    if type(a) != float:
        print("Same types")
        print("Another print")
    print("Outside of if block")

    print(id(a))

    print(type(a))
    print(type(b))
    """

    '''
    try:
        print(solveProblem1(10, 3))
        print(solveProblem1(7, 3))
        print(solveProblem1(3, 4))
        #print(solveProblem1("abc", 4))
        print(solveProblem1("abc", "bc"))
    except TypeError:
        print("All variables in this program need to be integers")

    a = "abc"
    b = "bc"

    print(a + b)
    print(b + a)
    '''

    #print(FizzBuzz())

    """
    try:
        n = int(input("Number of Fibonacci Terms: "))
        print(computeNFibonacciTerms(n))
    except ValueError:
        print("The number of Fibonacci terms should be an integer")
    """

    #print(round(computeBodyMassIndex(80.0, 1.70), 3))

    n = int(input("Number of elements: "))
    luckyList = []
    for i in range(n):
        elem = int(input("Elem: "))
        luckyList.append(elem)

    print(computeLuckySum(luckyList))

main()
