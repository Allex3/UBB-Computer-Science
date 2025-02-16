"""
    Determine the time complexity of the following algorithms as a function of n.
    sources:
        https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
        https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/

    Algorithm complexity (time)
        n - size of the algorithm's input (in many cases its the length of a list, rows of a matrix, some index)
        T(n) - function which provides the number of operations the algorithm makes for input size n

        once we have the expression for T(n) we can provide the algorithm complexity as follows:
            T(n) = 2 * n^2 + n - 1
            1. Only consider the dominating term (the term at the highest power)
            2. Remove the constants
        Then we have the complexity:
            Theta(n) - both high and low bound (it does not necessarily exist)
            O(n)     - high bound (the algorithm cannot surpass this complexity)
            Omega(n) - low bound (the algorithm cannot fall below this complexity)

    Obs:
        - Every operation that does not depend on "n" is assumed to take 1 unit of time
        - Constant time is not necessarily short (wait for the weekend is constant time)
"""
from random import random


# T(n) = 10 * n * 1 => Theta(n)
def f_1(n: int):
    for i in range(10):  # O(1)
        for j in range(n):  # liniar time O(n)
            print("Hello World")  # constant time O(1)


# T(n) = 10 * n * 1 => Theta(n)
def f_2(n: int):
    for i in range(n, n + 10):  # n, n + 1, ..., n + 9 (constant time) => O(1)
        for j in range(n):  # 0, ..., n
            print("Hello World")


# T(n) = (1, ..., n - 1) + (2, ..., n - 1) + ... + (n - 1) => (n-1)(n-2)/2 => O(n^2)
#        (values of j)
def f_3(n: int):
    for i in range(1, n):  # O(n)
        for j in range(i, n):
            print("Hello World")


# T(n) = 2*n^2 => O(n^2)
def f_4(n: int):
    for i in range(n):  # O(n)
        for j in range(2 * i + 1):  # max value is (2n  - 1) => O(n)
            print("Hello World")


# T(n) = n^4 => O(n^4)
count = 0


def f_5(n: int):
    global count  # consider the global count variable
    for i in range(n ** 2):  # O(n^2)
        for j in range(i):  # O(n^2)
            # print("Hello World")
            count += 1


# empirical evaluation :)
# for i in range(1, 31):
#     count = 0
#     f_5(i)
#     print(i, count)

# T(n) = n * log_2(n) so the algorithm is O(n*log_2(n))
def f_6(n: int):
    for i in range(n):  # n
        t = 1
        while t < n:  # we approximate log_2(n) each time, even if that's only the last run
            print("Hello World")
            t *= 2  # we can multiply "t" a number of log_2(n) times before it's greater than "n"


"""
    Time complexity depends on both "n" and "m"
"""


# T(n, m) = n + m => O(n+m)
def f_7(n, m: int):
    for i in range(0, n):  # n loops
        print("Hello World")
    for j in range(0, m):  # m loops
        print("Hello World")


# T(n, m) = 2n => O(n)
def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


# T(n) = 2 * n^2 => O(n^2)
def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


# T(n) = n^2 => Theta(n^2)
def f_10(n: int):
    for i in range(n):  # n
        for j in range(n, i, -1):  # n -> i + 1 => n / 2
            print("Hello World")


# T(n, m) = n + m => Theta(n+m)
def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n):
        a = a + random()  # what's the time complexity of random()?, we assume that its O(1)

    for i in range(m):
        b = b + random()


# T(n) = n/2 * log_2(n) => Theta(n * log_2(n))
def f_12(n: int) -> None:
    k = 0
    for i in range(n // 2, n):  # // is integer division => n/2 times
        j = 2
        for j in range(2, n, pow(2, j)):  # log_2(n)
            k = k + n / 2


"""
    Analyze the time and space complexity 
"""

"""
Time complexity
    n = len(data)
    T(n) = n * log_3(n) => Theta(n * log_3(n))
    
Space complexity
    T(n) = 1 => Theta(1) # the allocated memory does not depend on the length of the list
"""


def f_13(data: list) -> int:
    data_sum = 0
    for el in data:  # O(n)
        j = len(data)  # j = n
        while j > 1:  # O(log_3(n))
            data_sum += el * j
            j = j // 3
    return data_sum


"""
Time complexity
    n = len(data)
    
    T(n) = 1, if n < 2
    T(n) = 2 * T(n/2) + 1, n >= 2
    
    T(n) = 2 * T(n/2) + 1
    T(n/2) = 2 * T(n/4) + 1
    T(n/4) = 2 * T(n/8) + 1
    
    T(n) = 2 * [2 * T(n/4) + 1] + 1
    T(n) = 4 * T(n/4) + 2 + 1
    T(n) = 4 * [2 * T(n/8) + 1] + 2 + 1
    T(n) = 8 * T(n/8) + 4 + 2 + 1
    
    T(n) = 16 * T(n/16) + 8 + 4 + 2 + 1
    there exists a value k so that 2^k = n (or k = log_2(n) )
    what do we get after "k" iterations?
    
    T(n) = 2^k * 1 + 2^(k-1) + ... + 2^0 = 2^(k+1) => O(n)
    
Space complexity
    T(n) = 2 * T(n/2) + n (n is from the 2 slices of the original list) 
    ...
"""


# TODO Continue the calculation for space complexity


def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    """
    What happens on the follosing line? 
    1. Slices of the data list are created (data[:m]) -> part of the list is copied
    2. f_14 is called (twice, in succession)
    3. The + operation is carried out
    4. Function returns
    """
    return f_14(data[:m]) + f_14(data[m:])


def f_15(n: int) -> int:
    s = 0
    for i in range(1, n ** 2):
        j = i
        while j != 0:
            s = s + j - 10 * j // 10
            j //= 10
    return s


def f_16(n, i: int) -> None:
    if n > 1:
        i *= 2
        m = n // 2
        f_16(m, i - 2)
        f_16(m, i - 1)
        f_16(m, i + 2)
        f_16(m, i + 1)
    else:
        print(i)


"""
Analyze the algorithm's time complexity. Write an equivalent algorithm with 
a strictly better time complexity
"""


def f_17(data: list) -> int:
    i = 0
    j = 0
    m = 0
    c = 0
    while i < len(data):
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data):
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m


"""
    What is the time complexity when implementing the following algorithm. How can this be 
    optimized and how will that improve the complexity?
"""


def f_18(x, n: int):
    """
    The algorithm returns x ** n
    :param x:
    :param n:
    :return:
    """
    # TODO Implement me
    pass
