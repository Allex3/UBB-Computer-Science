"""
    Determine the time complexity of the following algorithms as a function of n.
    sources:
        https://complex-systems-ai.com/en/algorithmic/corrected-exercises-time-complexity/
        https://www.geeksforgeeks.org/practice-questions-time-complexity-analysis/
"""
from random import random

"""
    Time complexity notation:
        n - size of the algorithm's input (length of the list, number of elements of a matrix, an index)
        T(n) - function that represents the number of operations carried out by the algorithm for input size n
        # T(n) = 2 * n leads to linear time
        
        after we calculate/approximate T(n) we can talk about the time complexity
        Going from T(n) to time complexity:
            1. Only consider the dominating term (when n grows large)
            2. Throw out any constants
        Algorithm complexity:
            BigO => O(n) -> high bound on algorithm complexity (algorithm cannot be slower than this)
            BigOmega => Omega(n) -> low bound on algorithm complexity (algorithm cannot be faster than this)
            Theta => Theta(n) -> the exact complexity (both low and high bound), not sure this exists!?
    Extra-space complexity
        - how much additional memory space the algorithm requires to do its job
        - we do not consider the input
        
    Notes:
        -> Every operation that does not depend on "n" takes 1 unit of time
        -> Function allocates a quantity of memory that does not depend on "n" -> 1 unit of space :) 
"""


# T(n) = 10 * n * 1 => Theta(n), O(n)
def f_1(n: int):  # input size is given by the value of input parameter n
    for i in range(10):  # i is between 0 and 9 => 10 times => O(n) due to the inner loop
        for j in range(n):  # j is between 0 and n - 1 => n times => O(n)
            print("Hello World")  # O(1)


# T(n) = 10 * n * 1 => Theta(n)
# the first for loop runs for 10 iterations regardless of n's value
def f_2(n: int):
    for i in range(n, n + 10):  # n, ..., n + 9 => O(1)
        for j in range(n):  # O(n)
            print("Hello World")


# T(n) = (n-1) + (n-2) + ... + 1 = n(n-1)/2 => Theta(n^2)
def f_3(n: int):
    for i in range(1, n):  # n steps, so O(n)
        for j in range(i, n):  # (1,2, ..., n-1), (2,...,n-1), ..., (n-1) - number of iterations
            print("Hello World")


# T(n) = n * (2n-1) => 2n^2 - n => Theta(n^2)
def f_4(n: int):
    for i in range(n):  # n steps, so O(n)
        for j in range(2 * i + 1):  # (0), (0,1,2), (0,1,2,3,4,5,6), ..., (0,...,2n-1)
            # approximate we go to 2n-1 each time => larger number of steps
            print("Hello World")


counter = 0


# T(n) = n^2 * n^2 => Theta(n^4)
def f_5(n: int):
    global counter  # consider the module-level variable counter
    for i in range(n ** 2):  # n^2 (starts at 0, ends at n^2 - 1)
        for j in range(i):  # n^2
            # print("Hello World")  # O(1)
            counter += 1


# for index in range(1, 31):
#     f_5(index)
#     print(index, counter)
#     counter = 0

# sum = 0
# for i in list(range(1_000_000_000)):
#     sum += i
#
# print(sum)

# T(n) = n * log_2(n) => Theta(n * log_2(n))
def f_6(n: int):
    for i in range(n):  # n steps
        t = 1
        while t < n:  # runs log_2(n) times
            print("Hello World")
            t *= 2


"""
    Time complexity depends on both "n" and "m"
"""


# T(n, m) = n + m => Theta(n + m)
def f_7(n, m: int):
    for i in range(0, n):  # n loops
        print("Hello World")
    for j in range(0, m):  # m loops
        print("Hello World")


# T(n) = 2 * n => Theta(n)
def f_8(n, m: int):
    for i in range(0, n):
        print("Hello World")
    for j in range(0, n):
        print("Hello World")


# T(n) = 2*n * n => Theta(n^2)
def f_9(n: int):
    for i in range(n):
        for j in range(n):
            print("Hello World")
        for k in range(n):
            print("Hello World")


# T(n) = n^2
def f_10(n: int):
    for i in range(n):
        for j in range(n, i, -1):  # between n and i, decreasing by 1
            print("Hello World")


def f_11(n: int, m: int) -> None:
    a = 0
    b = 0
    for i in range(n):
        a = a + random()

    for i in range(m):
        b = b + random()


def f_12(n: int) -> None:
    k = 0
    for i in range(n // 2, n):
        for j in range(2, n, pow(2, j)):
            k = k + n / 2


"""
    Analyze the time and space complexity 
"""

"""
    Time complexity
        n = len(data)
        Theta(n * log_3(n))
    
    Extra-space complexity
        data = initial list, we do not count it
        O(1) because we don't allocate memory space based on the size of the initial input
"""


def f_13(data: list) -> int:
    data_sum = 0
    for el in data:  # runs n times
        j = len(data)  # j = n
        while j > 1:  # log_3(n)
            data_sum += el * j
            j = j // 3
    return data_sum


"""
    Time complexity:
        n = len(data)

    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + 1, n >= 2
    
    T(n) = 2 * T(n/2) + 1
    T(n/2) = 2 * T(n/4) + 1
    T(n/4) = 2 * T(n/8) + 1
    T(n/8) = 2 * T(n/16) + 1
    
    T(n) = 2 * [2 * T(n/4) + 1] + 1
    T(n) = 4 * T(n/4) + 2 + 1
    T(n) = 4 * [2 * T(n/8) + 1] + 2 + 1
    T(n) = 8 * T(n/8) + 4 + 2 + 1
    
    T(n) = 16 * T(n/16) + 8 + 4 + 2 + 1
    at one point we get lists of length 1
    at that point we divided the list k times, so 2^k = n 
    so ...
    T(n) = 2^k * T(1) + 2^(k-1) + 2^(k-2) + ... + 2^0 # remember that T(1) = 1, base case of the recursion :)
    T(n) = (2^(k+1) - 1) / (2 - 1) # known formula
    T(n) = 2n - 1 => Theta(n)
    
    # assuming that data[:m] is an O(1) operation!
    
    Space complexity!
        n = len(data)
        
    T(n) = 1, n < 2
    T(n) = 2 * T(n/2) + n, n >= 2
"""


# TODO Make the calculation for space complexity, like in the case of time complexity

def f_14(data: list) -> int:
    if len(data) == 0:
        return 0
    if len(data) == 1:
        return data[0]
    m = len(data) // 2
    return f_14(data[:m]) + f_14(data[m:])  # if n = len(data), then n/2 = len(data[:m])


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
    while i < len(data):  # n steps
        if data[i] == data[j]:
            c += 1
        j += 1
        if j >= len(data):  # n - 1, n - 2, ..., 1 steps
            if c > m:
                m = c
            c = 0
            i += 1
            j = i
    return m


"""
1. Determines the frequency of the element that appears most often in the list
2. Time complexity is Theta(n^2)
"""


def f_17_better(data: list) -> int:
    map = {}
    for e in data:  # O(n)
        if e in map:
            map[e] += 1
        else:
            map[e] = 1

    max_freq = 0
    for key in map:  # O(n)
        max_freq = max(max_freq, map[key])
        # if map[key] > max_freq:
        #     max_freq = map[key]
    return max_freq


print(f_17([1, 2, 2, 2, 3, 3, 1]))

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
