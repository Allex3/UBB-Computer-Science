import itertools
def getNumberOfPartitions(n: int) -> int:
    """
    Function to get the number of partitions of a set A
    """
    """
    The Bell number Bn counts the different ways to partition a set that has exactly n elements, or equivalently, it counts the number of equivalence relations on it.
    Let's denote by S(n, k) the number of ways to partition a set with n elements
        into k non-empty subsets (each partition has exactly k sets)
    Of course, by this definition, the Bell number Bn is the sum of all S(n, k) with k going from 0 to n (we get all the partitions with 1 set, 2 sets, ..., n sets, so basically all the possible partitions)
    
    This is helpful because those numbers S(n, k) can be calculated using a recurrent formula:
        S(n, k) = k*S(n-1, k) + S(n-1, k-1)
    Explanation:
        To obtain the number of partitions of a set with n elements that have exactly k sets from the previous iteration, i.e., the partitions of a set with n-1 elements into exactly k subsets
        First of all, we could have a set with n-1 elements and the same number of sets in the partitions, in which case, we add the new element in ANY set of the partition, and there are K sets, hence k*S(n-1, k)
        Secondly, we add the element to the set that has n-1 elements, but also partitions of k-1 sets, so in this way, the new element MUST go in a new set in the partition, so it's only 1*S(n-1, k-1)
    
    we can start by saying that S(1, 1) = 1, to start from there
    S(n, k) where k>n is always 0, you can't partition n elements into n+1 or n+2 or... elements, so always just iterate from 1 to the current cardinality 
        that we're checking, that is the k, no reason to go beyond that, it will always be 0
    
    But, we don't need a matrix of all the possible pairs that takes nxn memory
    It's enough to have a 2xn matrix, so the memory being occupied is way less
    because at every "row" denoted by n in S(n, k)
    we only use the row above it, i.e. S(n-1, k=1, 2, ..., n), where n is the current cardinality being checked
    So we only need two rows, and the final results will be at the end on the
        second row, which denotes S(n, k), where n=n and k=1, 2, ..., n
        The sum of that final row is the Bell number n, i.e., for our set A
    
    https://en.wikipedia.org/wiki/Bell_number
    https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
    """
    #n is the length of set A, it's cardinality
    #I will use a dictionary with a pair of elements, instead of a matrix
    S = dict()
    #And at the end of each iteration for the current cardinality
    #   We will make the first row be equal to the current second row
    #   And the second row have only elements of value 0
    #This represents that we go "down" one row in the "matrix"
    #So let's define the two rows of the dictionary to have two rows of length n with all elements 0, representing rn S(1, k) and S(2, k), k=1, 2, .., n
    #   With S(2, k) all being 0, not calculated yet, and S(1, k) being all 0 beside S(1, 1)
    for i in range(0, n+1): #also start from 0 to be 0, because when k=1 it is accessed
        S[(1, i)] = 0
        S[(2, i)] = 0
    S[(1, 1)] = 1

    for i in range(2, n+1): #from 2 to n, (1, k) is 0 for any k>=2 and 1 for k=1 already
        for k in range(1, i+1): #1 to i; don't go beyond i, because everything is 0 there already
            #and we know that S(i, k) = 0 for any k>i
            S[(2, k)] = k*S[(1, k)] + S[(1, k-1)]
            # the above assignment <=> S(i, k) = k*S(i-1, k) + S(i-1, k-1)

        for k in range(1, i+1): #make the first row = the second row and reset the second row
            # Go only from 1 to i, the others were never used because i was only smaller
            # The elements bigger than i are 0, they were never worked with
            S[(1, k)] = S[(2, k)]
            S[(2, k)] = 0

    #Since after the last iteration, the second row that was calculated was moved in the first row
    #The S(n, k), k=1, 2, ..., n results are in S[(1, k)], k=1, 2, ..., n
    #As said before, add them up to obtain the bell number we return
    Bn = 0
    for k in range(1, n+1):
        Bn += S[(1, k)]

    return Bn

#user interaction

def output():
    """
    The function that outputs the results for problems 1 and 2
    """
    fileNumber = getUserInput() #the number of the input and its respective ouput
    inputFile = open(f"inputs/input{fileNumber}.txt", "r") #read from the file that contains the fileNumber'th input
    outputFile = open(f"outputs/output{fileNumber}.txt", "a") #append to the file that contains the output
    n = int(inputFile.read())  # read the file input (cardinality of set A)

    # 1. the number of partitions on a set A = {a1, a2, ..., an}
    #get the number of partitions on a set from the

    #For the sake of simplicy of not being able to write a_1, I will
    # use A={1, 2, ..., n}
    # and for the graph delta_A i will use ∆ = {(1, 1), (2, 2), ..., (n, n)}

    outputFile.write(str(getNumberOfPartitions(n))) #where n = cardinality of set A, so
    #in our case, the set A={1, 2, ..., n}


    '''
    2. the partitions on a set A = {a1, . . . , an} and their corresponding equivalence relations (for n ≤ 8)
    '''

def getUserInput():
    try:
        n = int(input("What input file do you want to run on (1-5): "))
        if (n<=0): #n not natural, ask again
            print("Your input is not a non-zero natural number. Try again")
            return getUserInput()
        elif (n>5): #input file above 5 does not exist
            print("Your input is not between 0-5. Try again")
            return getUserInput()
        return n
    except ValueError:
        print("Your input is not an integer. Try again")
        return getUserInput() #run recursively until you get an integer and return it (if try works)

if __name__ == '__main__':
    output()
