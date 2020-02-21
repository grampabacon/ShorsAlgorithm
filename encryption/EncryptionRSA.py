import random


class RSAEncryption:

    def generate_keypair(p, q):
        if not (is_prime(p) and is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')
        # n = pq
        n = p * q

        # Phi is the totient of n
        phi = (p - 1) * (q - 1)

        # Choose an integer e such that e and phi(n) are coprime
        e = random.randrange(1, phi)

        # Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)

        # Use Extended Euclid's Algorithm to generate the private key
        d = multiplicative_inverse(e, phi)

        # Return public and private keypair
        # Public key is (e, n) and private key is (d, n)
        return ((e, n), (d, n))