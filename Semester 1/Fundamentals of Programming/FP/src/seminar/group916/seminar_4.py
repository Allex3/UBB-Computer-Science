"""
    Problem Solving Methods -- Divide & Conquer, Backtracking

    How does divide and conquer work?

    Divide & Conquer
    Divide: divide problem in sub-problems which are similar to the original (disjoint sub-problems)
    Conquer: solve the smallest problems
    Combine: combine the result obtained for the smaller problems (to solve the original one)


    What D&C algorithms do we already know?

    Merge sort, Binary search, Quick sort

    Divide: divide the list into halves
    Conquer: array of length 1 is sorted
    Combine: merge the sorted lists
"""

"""
    1. Implement an optimized version of the merge sort algorithm
        a. Implement Merge Sort
        b. Use the insertion sorting algorithm with the binary search optimization found in the lecture examples
        c. Time the resulting version using the ex17_sort_comparison.py example - at home
        d. Discuss how merging might be improved using exponential search
"""

# Ratiu Mihai Cornel
def merge_sort(array, thershold=10) -> list:
    if len(array) <= 1:
        return array

    if len(array) <= thershold:
        return insertionSort(array)

    m = len(array) // 2

    list1 = merge_sort(array[:m])
    list2 = merge_sort(array[m:])

    return merge(list1, list2)


def merge(list1, list2) -> list:
    output = []

    idxi = 0
    idxj = 0

    while idxi < len(list1) and idxj < len(list2):
        if list1[idxi] < list2[idxj]:
            output.append(list1[idxi])
            idxi+=1
        else:
            output.append(list2[idxj])
            idxj+=1

    while idxi < len(list1):
        output.append(list1[idxi])
        idxi+=1

    while idxj < len(list2):
        output.append(list2[idxj])
        idxj+=1

    return output

#Simon Laszlo
def binarySearch(list, low:int, high:int, n:int) -> int:
    while low < high:
        mid = (low + high) // 2
        if n > list[mid]:
            low = mid + 1
        elif n < list[mid]:
            high = mid - 1
        else:
            return mid
    return low

def insertionSort(listToBeSorted):
    for i in range (len(listToBeSorted)):
        val = listToBeSorted[i]
        pos = binarySearch(listToBeSorted, 0, i, val)
        listToBeSorted = listToBeSorted[:pos] + [val] + listToBeSorted[pos:i] + listToBeSorted[i+1:]
    return listToBeSorted

"""
    2. Find the smallest number in a list using a recursive divide & conquer implementation. Return None for an empty 
    list. Implement the following variants:
        a. Chip & conquer (data of size 1 and data of size n - 1)
        b. Divide the list into halves
"""

#Muresan Ianis Group915
def chip_conquer(list):
    if len(list) == 0:
        return None

    if len(list) == 1:
        return list[0]

    return min(list[0],chip_conquer(list[1:]))

def divide_half(list):
    if len(list)==0:
        return None
    if len(list) == 1:
        return list[0]
    mid=len(list)//2
    return min(divide_half(list[:mid]),divide_half(list[mid:]))


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

def maximum_subarray(array: list):
    max_sum = float('-inf')
    for i in range(len(array)):
        current_sum = 0
        for j in range(i, len(array)):
            current_sum += array[j]
            max_sum = max(max_sum, current_sum)

    return  max_sum

# TODO
def maximum_subarray_divide_and_conquer(array: list):
    pass

def main():
    #toBeSorted = [2, -5, 100, 10, 81]
    #sorted = insertionSort(toBeSorted)
    #print(sorted)

    list = [-2, -5, 6, -2, -3, 1, 5, -6]
    print(maximum_subarray(list))

main()

"""
    Backtracking template

    We have a template that we need to customize.
        1. How is the search space represented (values in array X)
        2. When is array X consistent (consistent function)
            -> True if we can reach a solution strictly by adding values
            -> False otherwise
        3. When do we have a solution
            -> depends on the problem
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
    
    
    Board - Not OK
    n = 7
    
    R1: _ _ _ _ _ _ Q
    R2: Q _ _ _ _ _ _
    R3: _ _ Q _ _ _ _
    R4: _ _ _ _ Q _ _
    R5: _ Q _ _ _ _ _
    R6: _ _ _ Q _ _ _
    R7: _ _ _ _ _ Q _
    
    Conditions: 2 queens are not allowed to be on the same row
                2 queens are not allowed to be on the same column 
                2 queens are not allowed to be on diagonal
                
    Search space: X = [1, ...., n]
    X[i] = the column on which the queen from row i is 
    
    Consistent: 1. Already done
                2. X[i] != X[j], for all i != j 
                3. |X[i] - X[j]| != |i - j|, for all i != j from the search space
                
    Solution: len(X) = n, meaning that we placed all the queens on the board
"""

#Stanculescu Andrada-Cristina
def consistent(x):
    """
    Determines whether the current partial array can lead to a solution
    """
    currentRow=len(x)-1

    for i in range(len(x)-1):
        if(x[i] == x[currentRow] or abs(x[i] - x[currentRow]) == abs ( i - currentRow ) ):
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




"""
    7. A Latin square is an n × n square filled with n different symbols, each occurring exactly once in each row and 
    exactly once in each column

    Generate all the N x N Latin squares for a given number N. 
"""

"""
    8. Generate all reduced N x N Latin squares for a given number N. In a reduced Latin square, the elements of the 
    first row and first column are sorted.
"""