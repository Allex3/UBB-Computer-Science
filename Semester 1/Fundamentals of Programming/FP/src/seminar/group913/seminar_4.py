"""
    Problem Solving Methods -- Divide & Conquer, Backtracking
"""

from random import randint, shuffle
from lecture.examples.ex13_insertion_sort import binary_insertion_sort

"""
    1. Implement an optimized version of the merge sort algorithm
        a. Implement Merge Sort
        b. Use the insertion sorting algorithm with the binary search optimization found in the lecture examples
        c. Time the resulting version using the ex17_sort_comparison.py example
        d. Discuss how merging might be improved using exponential search
"""


def merge(left: list, right: list) -> list:
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        result.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        result.append(right[right_index])
        right_index += 1

    return result


def merge_sort_913(data: list) -> list:
    # basic case of recursion
    if len(data) == 1:
        return data
    elif len(data) < 16:
        return binary_insertion_sort(data)

    m = len(data) // 2  # // is integer division
    return merge(merge_sort_913(data[:m]), merge_sort_913(data[m:]))


def gen_list(n: int) -> list:
    result = []

    while n > 0:
        result.append(randint(0, 100))
        n -= 1
    return result


def test_sort():
    for i in range(1_000):
        data = gen_list(randint(1, 100))
        sorted_merge = merge_sort_913(data)

        # assert followed by an expression fails if the expression is false
        # nothing happens if the expression is true
        assert sorted_merge == sorted(data)


test_sort()

# data = gen_list(5)
# print(data)
# shuffle(data)
# print(data)
# print(merge_sort(data))

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


def max_subarray_dynamic(data: list) -> int:
    max_global = data[0]
    max_current = data[0]
    for i in range(1, len(data)):
        if max_current > 0:
            # we extend the existing subarray with the current element
            max_current += data[i]
        else:
            # we start a new subarray
            max_current = data[i]

        # if max_current > max_global:
        #     max_global = max_current
        max_global = max(max_current, max_global)

    return max_global


# data = [-2, -5, -6, -2, -3, -1, -5, -6]
# print(max_subarray_dynamic(data))

"""
    5. All permutations of the {0, 2, ..., n - 1} set (recursive implementation)
"""


def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """

    # queens attack each other on the column
    if len(set(x)) != len(x):
        return False

    last_placed_queen = x[-1]

    for i in range(0, len(x) - 1):
        if abs(last_placed_queen - x[i]) == abs(i - len(x) + 1):
            return False
    return True


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


bkt_rec([], 4)

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
