"""
    Problem Solving Methods -- Divide & Conquer, Backtracking
"""
from random import shuffle, randint
from lecture.examples.ex13_insertion_sort import binary_insertion_sort

"""
    1. Implement an optimized version of the merge sort algorithm
        a. Implement Merge Sort
        b. Use the insertion sorting algorithm with the binary search optimization found in the lecture examples
        c. Time the resulting version using the ex17_sort_comparison.py example
        d. Discuss how merging might be improved using exponential search
"""


def gen_list(n: int) -> list:
    data = []
    while n > 0:
        data.append(randint(0, 200))
        n -= 1
    return data


def merge(list_one: list, list_two: list) -> list:
    result = []
    index_one = 0
    index_two = 0

    while index_one < len(list_one) and index_two < len(list_two):
        if list_one[index_one] < list_two[index_two]:
            result.append(list_one[index_one])
            index_one += 1
        else:
            result.append(list_two[index_two])
            index_two += 1

    # handle remaining elements
    #    result.extend(list_one[index_one:]) -- might be faster?

    while index_one < len(list_one):
        result.append(list_one[index_one])
        index_one += 1

    while index_two < len(list_two):
        result.append(list_two[index_two])
        index_two += 1

    return result


def merge_sort(data: list) -> list:
    # base case of the recursion, T(n) = 1
    if len(data) == 1:
        return data
    elif len(data) < 16: # how do we pick the threshold?
        return binary_insertion_sort(data)

    m = len(data) // 2  # // is integer division

    # sort the two halves -> T(n) = n extra space complexity
    left_half = merge_sort(data[:m])  # index m is exluced, just like the right parameter in range()
    right_half = merge_sort(data[m:])  # data[:] creates a copy of the list

    # merge into the original list
    return merge(left_half, right_half)


# data = [x for x in range(20, 0, -1)]
# res = merge_sort(data)


# data = list(range(20, 0, -1))
# data.sort(reverse=True) # reverse is a keyword argument
# print(data)
# print(res)

def test_sort():
    for i in range(1_000):
        data = gen_list(randint(1, 500))
        sorted_py = sorted(data)
        sorted_merge = merge_sort(data)

        # assert crashes the program if the expression is False
        assert sorted_py == sorted_merge


test_sort()

"""
    2. Find the smallest number in a list using a recursive divide & conquer implementation. Return None for an empty 
    list. Implement the following variants:
        a. Chip & conquer
        b. Divide the list into halves
"""

"""
    3. Calculate the r-th root of a given number x with a given precision p
"""

"""
    4. Calculate the maximum subarray sum (elements of a subarray have consecutive indices in the parent array)
        a. Naive implementation
        b. Divide & conquer implementation
        c. Dynamic programming implementation (next week)

        e.g.
        for data = [-2, -5, 6, -2, -3, 1, 5, -6], maximum subarray sum is 7.
"""

"""
    5. All permutations of the {0, 2, ..., n - 1} set (recursive implementation)
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    return len(set(x)) == len(x)


def solution(x, n):
    """
    Determines whether we have a solution
    """
    return len(x) == n


def solution_found(x):
    """
    What to do when a solution is found
    """
    print("Solution: ", x)


def bkt_rec(x, n):
    """
    Backtracking algorithm for permutations problem, recursive implementation
    """
    x.append(0)
    for i in range(0, n):
        x[len(x) - 1] = i
        if consistent(x):
            if solution(x, n):
                solution_found(x)
            else:
                bkt_rec(x[:], n)


# bkt_rec([], 4)

"""
    6. Change the code above to work for the n-Queen problem
"""

"""
    7. A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and 
    exactly once in each column

    Generate all the N x N Latin squares for a given number N. 
"""

"""
    8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the 
    first row and first column are sorted.
"""
