import numpy
import matplotlib.pyplot as plt

def get_partial_sums(N: int): #only compute the sum for a finite number of terms, that number is N
    sum_terms = [(-1)**(n+1) / n for n in range(1, N+1)]
    #make a list of the first N elements of the sum
    sum_terms = numpy.array(sum_terms)
    return numpy.cumsum(sum_terms) #return all the partial sums for those first N elements
    #i.e. s1, s2, ..., sn

# get the sum if we group them like firstly, p positive, then q negative, and this pattern repeats
def get_rearranged_partial_sums(p: int, q: int, N: int):
    pos_count, neg_count = 0, 0
    positive_term, negative_term = 1, 2  # start from the first positive term (1/1) and first negative term (-1/2)
    rearranged_partial_sums = []
    rearranged_sum = 0 #sum by rearranging the terms, add p positive then q negative
    terms_added = 0

    while terms_added < N: #only compute the rearranged sum for a finite number of terms, i.e. N
        # add p positive terms (elements with odd denominators are positive ((-1)^(n+1)/n) -> the exponent is even
        for _ in range(p):
            if terms_added >= N: #don't go beyond the maximum number of terms in the sum
                break
            rearranged_sum += 1 / positive_term
            positive_term += 2  # Move to the next positive term (odd denominators)
            terms_added += 1
            rearranged_partial_sums.append(rearranged_sum) #append to the partial sums the current sum (with a finite number of terms)
            # so rearranged_partial_sums[n] will be the sum of the first n elements of the rearranged sum

        # add q negative terms (elements with even denominators are negative ((-1)^(n+1)/n) -> the exponent is odd
        for _ in range(q):
            if terms_added >= N: #don't go beyond the maximum number of terms in the sum
                break
            rearranged_sum -= 1 / negative_term
            negative_term += 2  # Move to the next negative term (even denominators)
            terms_added += 1
            rearranged_partial_sums.append(rearranged_sum)

    return numpy.array(rearranged_partial_sums)

if __name__ == '__main__':
    N = int(input("For how many terms do you want to approximate the series (i.e. the partial sums of the first N terms are computed): ")) #I suggest 1000
    #for example, if we rearrange the sum as 1 - 1/2 - 1/4 + 1/3 - 1/6 - 1/8 + ... = 1/2 ln2, 1/2 of the original series
    p = int(input("Write the number of positive terms to be added first in the rearranged sum: "))
    q = int(input("Write the number of negative terms to be added after those p positive terms in the rearranged sum: "))

    # compute the partial sums for the original series
    ln_2 = numpy.log(2) # the original series we know should converge to ln(2)
    original_partial_sums = get_partial_sums(N)

    #get the rearranged partial sums using p and q, using the first N terms for it
    rearranged_partial_sums = get_rearranged_partial_sums(p, q, N)

    #original_partial_sums[N] and rearranged_partial_sums[N] are the sums with the first N elements, our approximation

    #now, to plot the two sums to show their difference, and ln(2) on a RxR 2D space
    plt.figure(figsize=(12, 6))
    plt.plot(original_partial_sums, label="Original Series Partial Sums", color="blue")
    plt.plot(rearranged_partial_sums, label=f"Rearranged Series (p={p}, q={q})", color="orange")
    plt.axhline(y=ln_2, color="red", linestyle="--", label="ln(2)")

    # Labels and title
    plt.xlabel("Number of Terms")
    plt.ylabel("Partial Sum")
    plt.title(f"Convergence of Alternating Harmonic Series vs. Rearranged Series (using the first {N} terms)")
    plt.legend()
    plt.grid(True)
    plt.show()

