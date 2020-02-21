import math
import timeit
import matplotlib.pyplot as plt
from functools import partial
import numpy as np


class TrialDivision:

    def __init__(self):
        print("Initialised.")

    def prime_factors(self, n):
        prime_factors = []

        while n % 2 == 0:
            prime_factors.append(2)
            n /= 2

        #  2 is the only even prime number, so skip all even numbers in the loop
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            #  if
            while n % i == 0:
                prime_factors.append(i)
                n /= i

        # Check if final value of n is greater than 2, if so it is a prime factor.
        if n > 2:
            prime_factors.append(n)

    def show_prime_factors(self, n):
        print("Factorising " + str(n) + ".")

        prime_factors = []

        while n % 2 == 0:
            prime_factors.append(2)
            n /= 2

        #  2 is the only even prime number, so skip all even numbers in the loop
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            #  if
            while n % i == 0:
                prime_factors.append(i)
                n /= i

        # Check if final value of n is greater than 2, if so it is a prime factor.
        if n > 2:
            prime_factors.append(n)

        # Print found prime factors
        print(prime_factors)

    """
    Run timer on function and plot time
    """
    def plot_time(self):
        max_n = 600000
        inputs = np.arange(int(max_n / 30), max_n, int(max_n / 30))
        x, y = [], []

        print(inputs)

        for i in inputs:
            timer = timeit.Timer(partial(self.prime_factors, i))
            t = timer.repeat(3, 20000)
            y.append(i)
            x.append(np.mean(t))

        plt.plot(x, y, 'ro')
        plt.xlabel("Time / s")
        plt.ylabel("Input")

        plt.show()


instance = TrialDivision()
instance.show_prime_factors(45)
# instance.prime_factors(600851475143999)
