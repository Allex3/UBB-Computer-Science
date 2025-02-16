"""
    Dynamic programming

    Optimality principle - the optimal solution to the problem includes optimal solutions to its subproblems
    Overlapping subproblems - in order to solve the problem we divide it into overlapping subproblems
    Memoization - remember the solutions of subproblems (so that we can access them quickly - O(1))
"""

"""
    1. Calculating the n-th term of the Fibonacci sequence
"""

"""
    Remember the complexities:
        time - O(2^n)
        space - O(n)
"""


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


"""
Using dynamic programming

    Remember the complexities:
        time (assume dict operations are constant) - O(n)
        space - O(n) (kind of 2 * n, one n is from building the cache, the other one from the recursion call stack)
"""
memo = {0: 0, 1: 1}  # {} is a set or dict, depending on how you initialize it


def fib_dp(n: int) -> int:
    print("n=" + str(n))
    if n not in memo:
        memo[n] = fib_dp(n - 2) + fib_dp(n - 1)
    return memo[n]


# fib_dp(10)
# for i in range(1, 11):
#     print(i, fib_dp(i))

"""
    2. Calculate the maximum subarray sum (subarray = elements having continuous indices)
"""
data = [-2, 5, -3, 1, -1, 2, -3, 4, 2, -10, -8]


def max_subarray(data: list) -> int:
    max_global = data[0]
    max_current = data[0]

    for i in range(1, len(data)):
        # the following lines are equivalent :)
        # max_current = max(data[i], max_current + data[i])
        max_current = data[i] if max_current <= 0 else max_current + data[i]

        # if max_current > 0:  # if max_current + data[i] > data[i]:
        #     max_current += data[i]
        # else:
        #     max_current = data[i]

        max_global = max(max_global, max_current)
        # if max_current > max_global:
        #     max_global = max_current
    return max_global


# print(max_subarray(data))

"""
    3. The knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that 
    you maximize the value of the stored items. Items can be broken up.
"""

"""
    4. 0-1 knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that 
    you maximize the value of the stored items. Items cannot be broken up (0-1 property).
"""
# W = 10  # total allowed weight
# weights = [6, 5, 5]  # object weights
# values = [7, 5, 5]  # object values

"""
    time complexity - O(2^n), where n is the number of objects
    space complexity - O(n), courtesy of the call stack :)
"""


def knapsack_naive(W: int, weights: list, values: list, current_object: int = 0) -> int:
    if current_object == len(weights):
        return 0

    value_include = 0
    if W >= weights[current_object]:
        value_include = values[current_object] + knapsack_naive(W - weights[current_object], weights, values,
                                                                current_object + 1)
    value_exclude = knapsack_naive(W, weights, values, current_object + 1)
    return max(value_exclude, value_include)


W = 12  # total allowed weight
weights = [3, 2, 4, 1, 6]  # object weights
values =  [4, 1, 5, 1, 6]  # object values

print(knapsack_naive(W, weights, values, 0))

"""
    5. Count in how many ways we can provide change to a given sum of money (N), when provided infinite supplies of the 
    given coin denominations.

    e.g. Let's say N = 10, and we have coins of values (1, 5, 10); we can give 
    change in 4 ways (10, 5 + 5, 5 + 1 + ... and 1 + ... + 1)
"""

"""
    6. The checkerboard problem
   https://www.geeksforgeeks.org/gold-mine-problem
"""
