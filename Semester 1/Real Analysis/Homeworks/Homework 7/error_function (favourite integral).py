import numpy as np
import matplotlib.pylab as plt
from math import exp #e^

def f(x):
    return exp(-x*x)

def compute_area_trapezoid(a: int) -> int:
    """
    Computes and returns the area by the trapezoid rule
    :param a: The constant a giving the interval [-a, a] for which to compute the area
    :return: The area numerical value
    """
    area = 0
    space = np.linspace(-a, a, max(5, int(a*5))) #minimum 5 if a < 1
    for i in range(1, len(space)):
        area += 0.5*(f(space[i]) + f(space[i-1]))*(space[i]-space[i-1]) # area of the trapezoid under the graph

    return area

def main():
    plt.figure()
    space = np.linspace(-3, 3, 100)
    plt.plot(space, [f(x) for x in space], label="$e^{-x^2}$")  # love latex
    plt.legend(loc="best")
    plt.show()

    plt.figure()
    a_space = np.linspace(1e-4, 3, 1000) #where sqrt pi will be plotted, space of all a's that give the intervals that i will test
    plt.xlabel("interval length")
    plt.ylabel("bell curve area")
    plt.plot(a_space, [np.pi**0.5 for _ in a_space], label = "$\sqrt{\pi}$")
    plt.plot(a_space, [compute_area_trapezoid(a) for a in a_space])
    plt.legend(loc = "best")
    plt.show()

    # So we can see, as a is getting bigger, the approximated area, that is the approximation of the integral
    # Gets closer and closer to sqrt(pi)

if __name__ == "__main__":
    main()