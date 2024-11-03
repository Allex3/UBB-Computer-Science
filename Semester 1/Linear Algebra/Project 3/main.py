"""
The vector space Z2^n consists of all n-dimensional binary vectors, where each element of the vector is either 0 or 1, i.e., each vector from Z2^n has the form (a1, a2, a3, ...., an), where a1, a2, ..., an are from {0, 1}, so each element of any vector from Z2^n can take two values, and that applies for all n elements, thus 2^n possible vectors in the vector space Z2^n

Since Z2^n is a canonical vector space, every basis of it has n vectors
For the linear independence of the vectors of the basis, each vector added to the basis MUST NOT be a linear combination of the previous vectors in the basis (negates the linear independence needed for the basis, since if one element can be a linear combination of the others it's linearly dependent) (it does NOT have a minimum number of generators)

Since we are in the vector space Z2^n over Z2, scalars are from Z2, so every vector can be multiplied with either 0 or 1 and added to the others, that's a linear combination

In this sort of binary space, if we add 1+1 is 0, 0+0 is 0, 0+1 = 1+0 = 1
This is the same as the truth table of the bitwise operation XOR wow
So any vectors added is the XOR of the components of the vectors
So a linear combination in this vector space is just the XOR of each first, second, ..., n-th components of the vectors added (if the scalar of a vector is 0, that vector is 0, and doesn't influence the others in XOR and is ignored, if it is 1 the vector remains the same)
So a linear combination in this vector space is 0 <=> The total number of 1s on a specific position k in each added vector in the linear combination is even (e.g. (1, 0, 1) + (0, 1, 0) + (1, 1, 1) = (1 xor 0 xor 1, 0 xor 1 xor 1, 1 xor 0 xor 1) = (0, 0, 0), because there are an even number of 1s being XORd

FORMULA FOR THE NUMBER OF BASES
    So a basis has n elements from Z2^n
    Choose any NON-ZERO vector as the first element of the basis, that is, 2^n-1 vectors to choose
    (since the null vector can be a linear comb. of any vectors (all scalars are 0), it is in all the linear combinations of the previous vector, so don't subtract it too)
    Now, for the second vector, it shouldn't be a linear combination of the first, so 0*v1 or 1*v1
        That is, from 2^n vectors, subtract 0*v1 and 1*v1, so 2^n-2
    For the third vector, it shouldn't be a linear combination of the first two
        Since for each vector we have the scalar options 0 or 1
        We have 2 scalar options for every vector in the linear combination
        So 2^2, that is, for the third vector, 2^n-2^2
    More generally, the k-th vector from the basis should NOT be a linear combination of the first k-1 vectors
    That is, 2 scalars for every vector of the linear combination, so 2 options for the first vector of the linear comb, 2 for the second and so on => 2^(k-1) linear combinations of the other vectors from the basis
    Thus, to add a k-th vector to the basis, we have 2^n-2^(k-1) options
    Since the first vector can be chosen 2^n-1 = 2^n-2^0 ways, the second 2^n-2^1 ways, the third 2^n-2^2 ways, ...
        until the last one that can be chosen 2^n-2^(n-1) ways, and multiply ALL of them
    THAT is the total number of basis of the vector space Z2^n over Z2

COMPUTING THE BASES
    The 2^n-1 total vectors (excluding the null vector) from the v.s. Z2^n can be represented as a binary number
        For example, the vector (0, 1, 1, 0) is the number 6, and wee see that in Z2^n a vector can be represented on a binary number of n digits maximum (bits)
        Because of this, we can say that all the possible vectors from the v.s. can be a number from 0 to 2^n-1 (but ignore 0)
        And their respective vector components are the bits of that number, so make a tuple of those number's bits, for each number

    Because n<=4, the time complexity doesn't really matter, so what we'll do is start a basis with every vector in the vector space and try to form a basis with it
    Then, to each such basis, try to add new vectors to it, again, from the 1 to 2^n-1 numbers that are actually vectors tuples
    For each added vector check if the basis we try to form is linearly independent. If not, don't add it to the basis

    (To check if a basis (set of vectors) is linearly independent in Z2^n, since we need to generate them only for n<=4, the time complexity doesn't matter that much)
    So just check them all (maximum of 4 vectors (for the basis) and 2 options for each one of them, for each element of the basis to check if it is a linear combination of the others (maximum 4 vectors, so maximum 2^3 options to check for each element, which there are maximum 4, so 2^3*4=32 maximum) and since for z2^4 there are 20000 bases, we can compute it in due time
    So, for each new added vector to the set, check if it's a linear combination of the vectors already in the set

    When we reach in a current basis n elements, print it, and pop the last element to go back and try to add another one
    Then do so for all the added vectors, after we came back in the function call (i.e. finished trying to add all the possible vectors after it, delete it and try another one at the same position)
    Using backtracking

"""

#Algorithms

def subset_linear_independent(vectors: list[int], vector_to_add) -> bool:
    vectorsNew = vectors[:] #make a copy of the subset and add the vector to it
    vectorsNew.append(vector_to_add)

    #any linear combination is basically, any oen element, then with any two elements,
    #then any three, then ... until n, so all the possible SUBSETS (combinations)
    #Make a stack and add to it all the subsets of all elements
    #And for any such combination, check if any elements of the vectorsNew set of n vectors can be made
    #And if so, then there is a linear combination of the basis that gives a vector of the basis
    #thus it is linearly dependent and not a basis, so return false
    stack = []
    for vector in vectorsNew:
        stack.append([vector])

    while stack:
        #check the current combination and make all the new ones
        combination = stack.pop()
        #XOR all the elements of a current subset, that's the linear combination
        #if the scalar is 0 the element isn't in the subset, otherwise it's 1 and XOR them
        #check the current combination, then make new ones from it

        combinationResult = 0  # start with 0000, so xor with 1 is 1 and xor with 0 remains the same
        for comb_vector in combination:
            combinationResult ^= comb_vector
        #check if any of this subset's vectors, beside the one in the current combination, can be obtained as a result of the current combination

        for vector in vectorsNew:
            if vector not in combination:
                if (combinationResult == vector):
                    return False

        #now make new combinations from the current one, by adding ALL the elements of the vectorsNew to it
        #without the ones that are already in it, those are new subsets with one more element
        for vector in vectorsNew:
            if vector not in combination:
                stack.append(combination + [vector])

    return True #if reached here all the linear combinations don't give any other vector from the basis
#so it is linearly independnet, thus a basis, return True





def get_all_vectors(n: int) -> list[int]:
    vectors = []
    for i in range(1, 2**n): #from 1 to 2^n-1, without the null vector
        #bits of the numbers from 1 to 2^n-1 represent all the possible vector of Z2^n
        #don't convert the number into a tuple of the bits, that is the vector itself
        #because it's easier to just keep it as a number to XOR the bits
        # for example, the number 10 in Z2^4 would be 1010, so (1, 0, 1, 0) vector
        vectors.append(i)
    return vectors



def compute_bases_impl(vectors:list[int], currentBasis: list[int], fileNumber: int, n:int) -> None:
    for vector in vectors:
        if (not currentBasis) or (subset_linear_independent(currentBasis, vector)) and not (vector in currentBasis):
            #so either form a new basis adding its first element, or check for the element we want to add
            # if the subset we're forming with it can become a basis, i.e. it is still linearly independent
            # or if the vector is already in the basis generators, ignore it
            currentBasis.append(vector)
            if (len(currentBasis) == n): #a basis should have n elements
                output_basis(currentBasis, fileNumber)
            else:
                compute_bases_impl(vectors, currentBasis, fileNumber, n)

            currentBasis.pop()

def compute_bases(n: int, fileNumber: int) -> None:
    all_vectors: list[int] = get_all_vectors(n) #list[int] of all vectors of the vector space
    compute_bases_impl(all_vectors, [], fileNumber, n)


def compute_number_of_bases(n: int) -> int:
    totalVectors = 2**n #2^n
    vectorsNotChosen = 1 #vectors we subtract from 2^n going forward at each added vector in the basis
    numberOfBases = 1
    for i in range(0, n): #go from 2^0 to 2^(n-1)
        # So to compute product (2^n-1)(2^n-2^1)(2^n-2^2)....(2^n-2^(n-1))
        # Start at 2^0 (already computed) and multiply 2 to it repeatedly until 2^(n-1)
        # each power of 2 is subtracted from 2^n and multiplied to the product
        numberOfBases *= (totalVectors - vectorsNotChosen)
        vectorsNotChosen *= 2 # (goes from 2^0 to 2^(n-1))

    return numberOfBases

#User interaction

def read_file(i):
    input_file = open(f"input{i}.txt", "r")
    n = int(input_file.read())
    input_file.close()
    return n

def output_basis(basis: list[int], fileNumber: int) -> None:
    output_file = open(f"output{fileNumber}.txt", "a")
    basisForm = []
    for vector in basis: #convert it to a vectro from a number
        vectorForm = []
        while vector:
            vectorForm.append(vector%2) #put the bits of vector in the vectorForm
            vector//=2 #go to next bit

        # since the vector should have n digits, we should add the insignificant 0es
        # for example, for number 1, we get only bit 1,
        #add insignificant zeroes to the right (they should be to the left, but we reverse it so to the right)
        while (len(vectorForm) < len(basis)): #len(basis) is n, from Z2^n, same number of elements in the basis
            vectorForm.append(0)
        vectorForm.reverse() #form the binary number by reversing the remainders of the repeated divisions
        basisForm.append(tuple(vectorForm))

    output_file.write(str(tuple(basisForm)) + "\n") #for it to show like ((), (), ..)
    output_file.close()

def output_number_of_bases(fileNumber, n, number_of_bases):
    output_file = open(f"output{fileNumber}.txt", "w")
    output_file.write(f"1. the number of bases of the vector space Z_2^{n} over Z_2 is {number_of_bases}\n")
    output_file.close()

def solve():
    for i in range(1, 6): #go through all the input files (1-5) and output them
        n = read_file(i)
        number_of_bases = compute_number_of_bases(n)
        output_number_of_bases(i, n, number_of_bases)
        if n>4: #if n is higher than 4 DO NOT output the vectors of each such bases
            continue
        #otherwise, compute them
        compute_bases(n, i)


if __name__ == "__main__":
    solve()