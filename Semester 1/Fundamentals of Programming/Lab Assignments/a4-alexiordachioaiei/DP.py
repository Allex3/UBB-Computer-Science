"""
Problem 2

Given the set of positive integers S and the natural number k, display one of the subsets of S which sum to k. For example, if S = { 2, 3, 5, 7, 8 } and k = 14, subset { 2, 5, 7 } sums to 14.
"""

def userInput() -> tuple[set, int]:
    try:
        S = set()
        n = int(input("n: "))
        if (n<=0):
            print("Your value should be higher than 0. Try again")
            return userInput()

        print("Write n unique numbers")
        for i in range(1, n+1):
            S.add(int(input(f"{i}'th number:")))

        k = int(input("Write k: "))
        return S, k
    except ValueError:
        print("Your values are not numbers. Try again")
        return userInput()


#T(n) = 2^n => O(n) = 2^n
def naive_approach(S: list, k:int, subset = [], index=0) -> list: #in the naive approach we just check all the subsets of S and display the first that has the sum k
    #This naive approach has the time complexity of 2^n, the number of subsets of S, there are 2^n of them
    # (number of combinations of n take k)
    #Since we need the SUBSETS, the order of the elements DOES NOT MATTER
    # for example, {2, 3, 5} is the same as {2, 5, 3}, {3, 2, 5}, ...
    # Because we are talking about subsets, not permutations or arrangements n take k
    #So how we generate them: Take the current element, then take ONLY THE NEXT ONE
    # Or exclude it and go to the one after that, in a recursive binary tree approach, this will take all of them
    # no need for a for from 1 to n, since we CANNOT have elements with a lower index
    # since the order does not matter, we only take the ascending order of the indexes

    if sum(subset) == k: #if we found a subset with sum k, return it
        #this will return the calls where it was returned and keep chaining until the beginning
        return subset

    # Clearly, if we passed all the elements in S, so index is outside of S, return
    # But also return if sum is higher than k, if we add any more elements the sum will still be higher and will never be k
    if index==len(S) or sum(subset) > k:
        return [] #return an EMPTY LIST

    include_in_subset = naive_approach(S, k, subset + [S[index]], index+1)
    #include the current element in the subset, and go to the next element to be checked
    if include_in_subset: #list not empty, return it
        return include_in_subset

    without_element = naive_approach(S, k, subset, index + 1) #just increment the index, without adding the subset
    return without_element #even if empty, return it to go back


#for the DP approach I will use a bottom-up method for it to be iterative
#So, a sum is composed of the elements of a set, and we want the last sub-problem to be used in our current problem
#To any sum from 1 to k, we choose if we add the CURRENT set element to it or not
#thus branching it, either adding the current element to make that sum, or not
#Let dp[i][j] represent if the sum j can be obtained from ANY COMBINATION of the the first i elements of the set S
# dp[i][j] = dp[i-1][j], if we EXCLUDE the current element, thus j (the sum) remains the same
# or       = dp[i-1][j-S[i-1]], thus "adding" S[i-1] to j
# (we subtract it, so that, if we do REACH 0, we know that j = sum of elements from S
# and of course only do j-S[i-1] if S[i-1]<=j
# if we get to a sum higher than 0 , and there's no element to make it 0
#then we can't obtain j from elements from the set S
#basically this means that their sum is always LOWER than j, but if it REACHES 0 it's exactly j
# but instead of adding them we subtract each one from j until we reach 0, same thing

#and, if S[i-1] > j, we can't add it to the sum, because it would be higher than j, so always exclude such elements
# thus, in such cases, dp[i][j] = dp[i-1][j]
#we run this, with a for with the elements of a set
#and in that for, a for with the sums, so we TRY to add the current set element to ALL the possible sums
# we need the for in for, because, the sum k is itself composed of many smaller sums
# that are already computed using elements of the set ,and we add other elements on top of those
# to get to k, so it's a dynamic programming approach

#now, the problem is how do we print THE SET that gives the sum?
# AFTER checking if the sum CAN be computed, for which the answer is in dp[n][k]
# (i.e. seeing if the sum k can be computed using any combination f the elements of the set S)
# we backtrack the sum using two pointers, starting from the sum k and last element of the set

# IF dp[i][j] = dp[i-1][j], it means the current element S[i-1] is NOT in our sum j
# because if it were, we could not have constructed it using S[i-2] too (S[i-2] is part of first i-1 elements)
# because it is indexed from 0
# (i.e. constructed using only the first i-1 elements)
# because it would have been added, so j would have had to get bigger
# since it doesn't, it means our sum j does not contain S[i], so go one index lower

#ELSE, it clearly means it is included in the sum, so append it to the set we want to print
# and lower the sum by S[i], and lower i by 1, because we already have it in the sum
# to check for now the sum j-S[i] and how can it be constructed with the first i-1 elements

# when we reach sum 0, it means we successfully obtained sum k
#or when the index i becomes 0, this means the sum begins with the first element of the set
#so j isn't zero yet, but we reached i=0

#simply, T(n, k) = n*k + n => O(n*k)
def DP(S: list, k: int) -> list:
    #first of all, make the set S a list so we can get indexed elements from it
    n = len(S)
    dp = [[False] * (k + 1) for _ in range(n + 1)] # matrix of (n+1) x (k+1)

    for i in range(n+1): # from 0 to n
        dp[i][0] = True #by convention, sum 0 can be composed of any elements
    # this happens because dp[i][j] will be made from dp[i-1][j-S[i-1]]
    # by this convention, if the sum reaches 0, dp[i][0] is TRUE for any combination of elements
    # thus it also makes all the dp[i][j]'s until there TRUE, if the sum reaches 0
    # S[i-1] is the current element i, because S is indexed from 0!!

    for i in range(1, n+1):
        for j in range(1, k+1):
            if S[i-1] > j: #current element is higher than the sum we want it to help compose
                #thus, ignore it and go to the next element for this particular sum
                dp[i][j] = dp[i-1][j] #the sum j using the first i elements is the same as the one using the first i-1 elements
            else: #Include OR exclude the current element from the sum, this time it's a choice
                dp[i][j] = (dp[i-1][j] or dp[i-1][j-S[i-1]])
                #or because, we need at least one of them to be true for the sum j to be computed

    #dp[n][k] -> if our sum k can be computed using at least ONE combination of the first n elements of the set
    # i.e. from all subsets from the set, and if that won't give k, then it cannot be computed
    print("The matrix dp:")
    print(end="    ")
    for i in range(0, k+1):
        print(i, end="     ") #print the numbers of the columns
    print() #newline

    rowNumber = 0
    for row in dp:
        print(rowNumber, end=" ")
        for column in row:
            print(column, end=" ")
        print()
        rowNumber += 1
    if not dp[n][k]:
        return []

    #if it can be computed, backtrack the sum to get the elements that it's made from
    i, j = n, k
    solution = []
    #start from the sum k being composed of any combination of the first n elements, so dp[n][k]
    while j>0: #while sum
        # hasn't reached 0
        if dp[i][j] == dp[i-1][j]: #element S[i-1] not included in the sum, because it can also be made from the first i-1 (until S[i-2]) elements of the set
            i-=1
        else: # it is in the sum
            solution.append(S[i-1])
            j-=S[i-1] #basically add it to the sum and go to a lower index to look for the sum until that index that is part of the k sum
            i-=1

    solution.reverse()
    return solution

def output_solution(k:int, solution: list) -> None:
    if not solution: # solution empty
        print(f"There is no subsequence which sums to {k}")
        return
    print(f"A subsequence which sums to {k} is {solution}")

def solve():
    S, k = userInput()
    solution = []
    S = list(S)
    choice = int(input("Type 1 for the DP approach and 2 for the naive, backtracking approach: "))
    if choice == 1:
        solution = DP(S, k)
    if choice == 2:
        solution = naive_approach(S, k)

    output_solution(k, solution)

if __name__ == "__main__":
    solve()