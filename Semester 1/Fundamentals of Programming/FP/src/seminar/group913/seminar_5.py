"""
    Dynamic programming

    Overlapping subproblems - solving the problem involves solving some overlapping subproblems
    Principle of optimality - the partial solutions are solutions of the subproblems themselves
    Memoization - Remember the solutions of the subproblems we already looked at
"""

"""
    1. Calculating the n-th term of the Fibonacci sequence
"""

"""
    time complexity - O(2^n)
    space complexity - O(n)
"""


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 2) + fib(n - 1)


memo = {0: 0, 1: 1}  # {} can  be a set or a dict

"""
    time complexity - O(n)
    space complexity - O(n) # one n from the memoization dict, one n from the call stack
"""


def fib_dp(n: int) -> int:
    if n not in memo:
        memo[n] = fib_dp(n - 2) + fib_dp(n - 1)
    return memo[n]  # suppose constant time


# for i in range(1, 11):
#     print(i, fib_dp(i))

"""
    2. Calculate the maximum subarray sum (subarray = elements having continuous indices)
"""

"""
    3. The knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that 
    you maximize the value of the stored items. Items can be broken up.
"""

"""
    4. 0-1 knapsack problem. Given the weights and values of N items, put them in a knapsack having capacity W so that 
    you maximize the value of the stored items. Items cannot be broken up (0-1 property).
"""
# W = 10  # knapsack weight
# weights = [8, 5, 5]
# values = [9, 5, 5]

"""
    time complexity - O(2^n), where n is the number of objects
    space complexity - O(n), where n is the number of objects
"""


def knapsack_naive(W: int, weights: list, values: list, current: int) -> int:
    if current == len(weights):
        return 0  # no objects left

    value_include = 0
    if W - weights[current] >= 0:
        value_include = values[current] + knapsack_naive(W - weights[current], weights, values, current + 1)
    value_exclude = knapsack_naive(W, weights, values, current + 1)

    return max(value_include, value_exclude)


W = 12
weights = [1, 2, 3, 4, 2]
values = [9, 4, 5, 6, 9]

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
