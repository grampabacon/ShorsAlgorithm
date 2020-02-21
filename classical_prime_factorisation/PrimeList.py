import numpy as np
import math


class PrimeList:

    def prime_factor(self, n):
        primes = self.prime_sieve(n)

        out = []
        for i in primes:
            if n % i == 0:
                out.append(i)

        print(out)

    def prime_sieve(self, approx_highest):
        sieve = [True] * (approx_highest + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(math.sqrt(approx_highest)) + 1):
            if sieve[i] == False:
                continue
            for pointer in range(i * i, approx_highest + 1, i):
                sieve[pointer] = False
        primes = []
        for i in range(approx_highest + 1):
            if sieve[i]:
                primes.append(i)
        return primes


instance = PrimeList()
instance.prime_factor(68615143)
