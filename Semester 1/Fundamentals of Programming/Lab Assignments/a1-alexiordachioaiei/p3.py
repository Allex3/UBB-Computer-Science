# Solve the problem from the third set here
#problem 13 from set 3

def solve(): #sort of main function
    print("This program will determine the n-th element of the sequence 1,2,3,2,5,2,3,7,2,3,2,5,... obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors")

    n = userInput()

    print("The n-th element of the sequence of primes is ", nthPrimeNumber(n))


def userInput(): #function that takes the user's input
    try: #if you input an integer this works and it outputs the solution
        n = int(input("Input your number: "))
        if (n<=0):
            print("Input a positive number higher than 0.")
            return userInput()
        return n
    except ValueError: # Your input is something else than an integer, so try again
        print("Your input is not an integer. Input again")
        return userInput()

def isPrime(n: int) -> bool: #this function checks if the number is prime
    for divisor in range(2, int(n**(1/2))+1, 1): #go from 2 to the square root of n and if it finds a divisor
        #until then, then the number is NOT prime
        if (n%divisor==0):
            return False
    
    return True

def getPrimeDivisors(n): #this function returns a list of the prime divisors of n
    if (isPrime(n)):
        return [n] #if the number is prime return a list of itself
    primeDivisors: list[int] = []
    for divisor in range(2, n//2+2, 1): #get the prime divisors of the number, going from 2 to itself/2+1
        #the only divisor it could be after n/2 is n itself, and if n is prime that case is handled above
        if n%divisor==0 and isPrime(divisor):
            primeDivisors.append(divisor)
    
    return primeDivisors

def nthPrimeNumber(n):
    if (n==1): #the first number of the sequence is 1
        return 1
    
    index = 2 #start at index 2 from the sequence of primes, case 1 is handled above
    currNumber = 2 #start at 1, case 1 is handled above
    while (True): #stop at nth number of the sequence
        #get the prime divisors of the currently checked number
        #(we basically iterate through the list of natural numbers higher than 1: 2, 3, 4, ...)
        primeDivisors = getPrimeDivisors(currNumber)
        #parse its prime divisors
        #if the number is prime this will just parse itself
        for primeDiv in primeDivisors:
            if (index==n):
                return primeDiv
            index+=1 #go to the next number in the sequence of prime numbers
        
        currNumber+=1

solve()


        
    