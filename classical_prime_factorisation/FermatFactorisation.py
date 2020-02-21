import numpy as np


class FermatFactorisation:

    """
    Uses fermat factorisation https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
    Crashes for prime number as N
    ineffective for even numbers
    """
    def prime_factor(self, n):
        max_n = np.ceil(np.sqrt(n))

        # Create an array of trial values to avoid use of loops.
        lim = min(n, 10 ** 6)  # 10E6 is a good number of elements to balance accuracy with performance.
        a = np.arange(max_n, max_n + lim)
        b2 = a ** 2 - n

        # Check whether b is a square number
        fracs = np.modf(np.sqrt(b2))[0]  # modf returns array of fractional parts.

        # Check for zero fractions (numbers with zero as their fractional part)
        indices = np.where(fracs == 0)

        # Find first occurence of a zero fraction
        # Flatten array
        a = np.ravel(np.take(a, indices))[0]
        a = int(a)
        b = np.sqrt(a ** 2 - n)
        c = a + b
        d = a - b

        if c == 1 or d == 1:
            return

        print(str(c) + " " + str(d))
        self.prime_factor(c)
        self.prime_factor(d)


instance = FermatFactorisation()
instance.prime_factor(3)
