"""
1. Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10
Question – What happens if we enter a non-integer number, or alphanumeric characters?
"""

"""
Function that checks if a, b or a + b is 10
:param a: should be of type int
:param b: should be of type int
Return: a boolean
        True is a or b is 10 or a + b is 10
        False otherwise
"""
def checkIfNumbersOrSumAre10(a, b):
    returnValue = False

    if type(a) != int or type(b) != int:
        return returnValue

    if a == 10 or b == 10 or a + b == 10:
        returnValue = True

    return returnValue


"""
2. Write a Python program which iterates the integers from 1 to 50. 
For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
For numbers which are multiples of both three and five print "FizzBuzz".
"""

def solveProblem2():
    for i in range(1, 50):
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
    if type(n) != int:
        raise TypeError("N needs to be an integer")

    if n <= 0:
        return []

    if n == 1:
        return [0]

    if n == 2:
        return [0, 1]

    fibonacciSequence = [0, 1]

    for i in range(2, n):
        fibonacciNewTerm = fibonacciSequence[-1] + fibonacciSequence[-2]
        fibonacciSequence.append(fibonacciNewTerm)

    return fibonacciSequence

"""
4. Write a Python program to calculate body mass index.
   How do we validate the code above for user input?
   Let's write the specification for it
"""

"""
Function that computes the body mass index, by the formula: BMI = weight / (height * height)
:param weight: the weight of the person, it should be in kg
               weight should be a strictly positive float
:param height: the height of the person, it should be in meters
       height should be a strictly positive float
:return Returns the body mass index
"""
def computeBodyMassIndex(weight, height):
    if type(weight) == int:
        weight = float(weight)

    if type(weight) != float or type(height) != float:
        raise TypeError("Weight and Height should be floats")

    if weight <= 0 or height <= 0:
        raise ValueError("Weight and Height should be strictly positive")

    return weight / (height * height)

"""
7. Return the sum of the numbers in a list, returning 0 for an empty list. Except the number 13 is very unlucky, 
so it does not count and numbers that come immediately after a 13 also do not count.
"""

def computeLuckySum(initialList):
    if len(initialList) == 0:
        return 0

    sum = 0

    '''
    for i in range(len(initialList)):
        if i == 0 and initialList[i] != 13:
            sum += initialList[i]
        elif i != 0 and initialList[i] != 13 and initialList[i - 1] != 13:
            sum += initialList[i]

    return sum
    '''

    if initialList[0] != 13:
        sum = initialList[0]

    for i in range(1, len(initialList)):
        if initialList[i] != 13 and initialList[i - 1] != 13:
            sum += initialList[i]

    return sum

def main():
    """
    print(checkIfNumbersOrSumAre10(10, 3))
    print(checkIfNumbersOrSumAre10(7, 3))
    print(checkIfNumbersOrSumAre10(5, 3))
    print(checkIfNumbersOrSumAre10("abc", 3))
    """
   # solveProblem2()
    '''
    try:
        print(computeNFibonacciTerms("abc"))
    except TypeError:
        print("Please use an integer for n")
    '''
    # print(computeBodyMassIndex(87, 1.86))

    inputFromConsole = []

    n = int(input("The number of elements of our list: "))

    for i in range(n):
        elem = int(input("Element = "))
        inputFromConsole.append(elem)

    print(computeLuckySum(inputFromConsole))


main()