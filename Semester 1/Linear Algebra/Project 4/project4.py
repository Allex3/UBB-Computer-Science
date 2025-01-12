def read_input(i: int) -> [int, int]:
    file = open(f"input_{i}.in", "rb")
    nk = file.read().split()
    n = int(nk[0])
    k = int(nk[1])
    return n, k


"""
Store, as in project 3, vectors as bitmasks of integers, for example
(0, 1, 0, 1) = 0101 = 5, and we know that if n=4, we only take the first 4 bits from the number
Because the XOR of the bits of an integer is the same as the addition of vectors in the vector space Z_2^n, the modulo 2 is simulated by the XOR on the bits.
Thus, the maximum bitmask of a vector is for the vector (1, 1, ..., 1) = 2^n-1
So we can store all the vectors from the vector space Z_2^n on bitmasks ranging from 0 to 2^n-1, so there are 2^n vectors in this vector space

Selecting only k of them for a k-dimensional subspace, we can take them in any order
Because it's a list, so the order does NOT matter, so we're talking about combinations, and that number is C_(2^n-1)^k, from 2^n-1 choose k, because we EXCLUDE the 0 vector from the list of vectors that can give a subspace, because it's redundant

Now, we have to check for a list of k vectors from the vector space, if they also give other vectors, in which case they will be part of the same k-dimensional subspace.
And this subspace has a basis of k vectors that give the subspace

Now, this k-dimensional subspace of Z_2^n actually behaves like the vector space Z_2^k
Because their dimension is the same, and the field is the same, so they form an isomorphism, the only difference are the vectors themselves, but the isomorphism is given by the dimension and coefficients from Z_2
Example: <(1, 0, 0), (0, 1, 0)> behaves like <(1, 0), (0, 1)> = Z_2^2
    since their number of unique linear combinations is the same and given by the COEFFICIENTS from the field Z_2, 0, a, b, a+b, so naturally, their number of linearly independent vectors is also the same
And the number, like in project 3, of linearly independent vectors from the subspace Z_2^k over Z_2 is (2^k-1)(2^k-2)(2^k-2^2)...(2^k-2^(k-1)) := LIK, ordered lists of linearly independent vectors
Basically choose all the vectors that are not a linear combination of the previous ones, which is trivial in Z_2^k, since we have only two choices for each coefficient from the linear combination
Thus, each k-dimensional subspace of the vector space Z_2^n has LIK ordered lists of linearly independent vectors, so here all the permutations of a list appear, so there are actually k! copies of the same list if it were to be a basis, because a basis does not have to be ordered

Now, we know also from Project 3, how to calculate the number of lists of k linearly independent vectors in Z_2^n:
    (2^n-1)(2^n-2)(2^n-2^2)....(2^n-2^(k-1))
But we know, these are ordered lists, so basically, each basis of a k-dimensional subspace appears k! times here

The thing is, a subspace is given by multiple basis, that are also in the above ordered lists of k linearly independent vectors, so how do we filter them out?
We know from before that there are LIK = (2^k-1)(2^k-2)(2^k-2^2)...(2^k-2^(k-1)) 
    ordered lists of k linearly independent vectors in any k-dimensional subspace of Z_2^n
    But since it's dimension itself is k, each of those lists is a basis for the subspace, and since it is ordered it appears k! times
Also, we know that this number accounts for ALL the ordered bases that give the subspace, these bases are also in the ordered linearly independent lists of k vectors in the Z_2^n vector space, and they give the SAME SUBSPACE!

So, if we were to divide these two products, we would successfully get rid not only of the permutations that are redundant of any bases, but also of the bases that give the SAME SUBSPACE, because their number is also in the LIK formula which we divide by
Thus, we will have EXACTLY the number of k-dimensional unique subspaces of Z_2^n
"""


def get_number_of_k_dimensional_subspaces(k: int, n: int) -> int:
    power2n = 2 ** n
    power2k = 2 ** k
    numerator = 1
    denominator = 1
    for i in range(0, k):
        numerator *= power2n - 2 ** i  # (2^n-1)(2^n-2)...(2^n-2^(k-1))
    for i in range(0, k):
        denominator *= power2k - 2 ** i  # (2^k-1)(2^k-2)...(2^k-2^(k-1))

    return numerator // denominator


# O(k log(k)) (k in the for loop, k for the 2**i, I assume it's logarithmic exponentiation

# to deal with the second part of the Project 4
# Since we only have to construct the basis for k<=n<=6, we can actually STORE the computed subspace
# And then, for every list of k linearly independent vectors from Z_2^n, check which vectors are formed as a linear combinations of those k vectors, and if that subspace is already computed, do not output that basis
# Compute the subspace by getting all the linear combinations of the vectors of the basis
# Each such linear combination gives a UNIQUE vector!
# But we also have to do this for EVERY linearly independent list of k vectors, and those are
# (2^n-1)(2^n-2)...(2^n-2^(k-1)), so we will have to check this many lists divided by k! to account for the ordered redundant lists

import numpy as np  # for matrix rank to check linear independence
from numpy.linalg import matrix_rank


def generate_vector_space(n: int) -> list[list[int]]:
    # just iterate through the vector's bitmasks 0 through 2^n-1 and repeatedly divide by 2 to construct the vectors
    # then reverse the list of components so it's in order from 1
    # (because by getting the modulo 2, the bits should be arranged in reverse order)
    vector_space = []
    # ignore the 0 vector because it's part of any subspace or linear combination possible, we don't use it
    for i in range(1, 2 ** n):
        vector = []
        aux = i
        while aux:
            vector.append(aux % 2)
            aux //= 2

        while len(vector) < n:  # for example if number is 5, 0101, we still need to add a 0 at the end to be all n components of the vector this bitmask represents
            vector.append(0)

        vector.reverse()
        vector_space.append(vector)

    return vector_space


def generate_all_linear_comb(basis: list[int], subspace: list[int], curr_lin_comb: list[int], index: int):
    if curr_lin_comb: #not empty, put it in the subspace if it's not already, check this subset linear comb.
        new_vector = basis[curr_lin_comb[0]] #start from the first vector of the lin. comb
        for i in range(1, len(curr_lin_comb)):
            new_vector ^= basis[curr_lin_comb[i]] # vector addition in Z_2^n

        if not (new_vector in subspace):
            subspace.append(new_vector)


    for i in range(index, len(basis)):
        # either take it or don't, if it's not already in
        curr_lin_comb.append(i)

        generate_all_linear_comb(basis, subspace, curr_lin_comb, i+1) #start from 1 more, so like the sets are in increasing order
        # especially because the order does not matter in a subset, so let it be the increasing order of the uniqueness
        curr_lin_comb.pop() # remove the current index and go to the next!


def build_subspace(basis: list[int], vectors: list[int]) -> set[int]:
    subspace = []
    for index in basis:
        subspace.append(vectors[index])

    generate_all_linear_comb([vectors[i] for i in basis], subspace, [], 0)

    #Now, since the subspace is build, make it a 'set' so it can be equal to all the other equivalent subspaces, since in a list the position of elements would be different
    # And append it to the list of subspaces
    if len(subspace) == 2**(len(basis))-1: #every subspace since it behaves like Z_2^k, it has 2^k-1 vectors
        return set(subspace)
    else:
        return {0}

def generate_linearly_independent_lists(n: int, k: int, vectors: list[int], vector_space: list[list[int]], subspaces: list[set[int]],
                                        lin_ind_list: list[int], fd: int, index: int) -> None:
    # Use the vectors in component format to check the linear independence using the rank of the matrix of the k vectors
    # But use the bitmask vectors to calculate the other vectors from this subspace!
    # And this works easily because vector_space[i] is equivalent to its bitmask at vectors[i]

    if len(lin_ind_list)==k: # check for linear independence
        A = []
        for index in lin_ind_list:
            A.append(vector_space[index])

        A = np.array(A) # make it a numpy array
        A = np.asmatrix(A) #make it a matrix

        if matrix_rank(A)==k: # if rank is k, they are linearly independent, so they form a subspace. Build it
            subspace = build_subspace([indexx for indexx in lin_ind_list], vectors)# build the subspace starting from these k vectors
            if not (subspace in subspaces) and subspace != {0}:
                subspaces.append(subspace)
                # we got a NEW subspace, so print its basis
                output_2(fd, lin_ind_list, vector_space)

        if len(subspaces)==100:
            pass
        return


    for i in range(index, 2**n-1): #start from 0 because vectors[0] = 1
        lin_ind_list.append(i)
        generate_linearly_independent_lists(n, k, vectors, vector_space, subspaces, lin_ind_list, fd, i+1)
        #store only the indexes to be easier
        lin_ind_list.pop()



def output_1(i: int, number_of_k_dimensional_subspaces: int, k: int, n: int) -> None:
    output_file = open(f"output_{i}.out", "w")
    output_file.write(
        f"1. the number of {k}-dimensional subspaces of the vector space Z_2^{n} over Z_2 is {number_of_k_dimensional_subspaces}")

    if n <= 6:
        output_file = open(f"output_{i}.out", "a")
        output_file.write("\n2. A basis of each such subspace is:")


def output_2(i: int, basis: list[int], vector_space: list[list[int]]) -> None:
    output_file = open(f"output_{i}.out", "a")
    basis_tuple = []
    for index in basis:
        basis_tuple.append(tuple(vector_space[index]))

    basis_tuple = tuple(basis_tuple) # turn to (()..())
    output_file.write(f"\n{basis_tuple}")



def solve() -> None:
    for i in range(3, 4):
        k, n = read_input(i)
        number_of_k_dimensional_subspaces = get_number_of_k_dimensional_subspaces(k, n)
        output_1(i, number_of_k_dimensional_subspaces, k, n)
        if n > 6:
            continue

        vectors = [i for i in range(1, 2 ** n)]
        vector_space = generate_vector_space(n)  # to check easier linear independence, also store vectors as they are, also for output
        subspaces = []
        generate_linearly_independent_lists(n, k, vectors, vector_space, subspaces, [], i, 0)


if __name__ == "__main__":
    solve()
