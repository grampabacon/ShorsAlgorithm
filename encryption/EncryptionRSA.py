import random
from classical.GreatestCommonDivisor import greatest_common_divisor
from util.PrimeChecker import is_prime_miller_rabin


class RSAEncryption:

    MAX_PRIME_LENGTH = 30

    def generate_random_prime(self):
        while True:
            random_prime = random.randint(10, self.MAX_PRIME_LENGTH)
            if self.is_prime(random_prime):
                return random_prime

    def generate_pq(self):
        p = self.generate_random_prime()
        q = self.generate_random_prime()
        while p == q:
            q = self.generate_random_prime()
        return p, q

    def is_prime(self, n):
        # low_primes is all primes (sans 2, which is covered by the bitwise and operator)
        # under 1000. taking n modulo each low Prime allows us to remove a huge chunk
        # of composite numbers from our potential pool without resorting to Rabin-Miller
        low_primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                      101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
                      181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269,
                      271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367,
                      373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461,
                      463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
                      577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661,
                      673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
                      787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883,
                      887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
        if n >= 3:
            if n & 1 != 0:
                for p in low_primes:
                    if n == p:
                        return True
                    if n % p == 0:
                        return False
                return is_prime_miller_rabin(n)
        return False

    def multiplicative_inverse(self, a, b):
        
        # Horrifying, messy code.
        # Euclid's extended algorithm for finding the multiplicative inverse of two numbers

        # Returns a tuple (r, i, j) such that r = gcd(a, b) = ia + jb
        
        # r = gcd(a,b) i = multiplicative inverse of a mod b
        #      or      j = multiplicative inverse of b mod a
        # Neg return values for i or j are made positive mod b or a respectively
        # Iterative Version is faster and uses much less stack space
        x = 0
        y = 1
        lx = 1
        ly = 0
        oa = a  # Remember original a/b to remove
        ob = b  # negative values from return results
        while b != 0:
            q = a // b
            (a, b) = (b, a % b)
            (x, lx) = ((lx - (q * x)), x)
            (y, ly) = ((ly - (q * y)), y)
        if lx < 0:
            lx += ob  # If neg wrap modulo orignal b
        if ly < 0:
            ly += oa  # If neg wrap modulo orignal a
        # return a , lx, ly  # Return only positive values
        return lx

    def multiplicative_inverse2(self, e, phi):
        d = None
        i = 1
        exit = False
        while not exit:
            temp1 = phi * i + 1
            d = float(temp1 / e)
            d_int = int(d)
            i += 1
            if (d_int == d) and d != e:
                exit = True
        return int(d)

    def generate_keypair(self, p=0, q=0):
        if p == 0 or q == 0:
            p, q = self.generate_pq()
        if not (self.is_prime(p) and self.is_prime(q)):
            raise ValueError('Both numbers must be prime.')
        elif p == q:
            raise ValueError('p and q cannot be equal')

        print("p: " + str(p) + "\nq: " + str(q))
        n = p * q

        # Phi is the totient of n
        phi = (p - 1) * (q - 1)

        # Choose an integer e such that e and phi(n) are coprime
        e = random.randrange(1, phi)

        # Use Euclid's Algorithm to verify that e and phi(n) are coprime
        g = greatest_common_divisor(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = greatest_common_divisor(e, phi)

        # Use Extended Euclid's Algorithm to generate the private key
        d = self.multiplicative_inverse2(e, phi)  # TODO: Make it so d != e ever.

        # Return public and private keypair
        # Public key is (e, n) and private key is (d, n)
        return (e, n), (d, n)

    def encrypt(self, public_key, plain_text):
        # Unpack the key into it's components
        e, n = public_key
        # Convert each letter in the plaintext to numbers based on the character using a^b mod m
        cipher = [pow(ord(char) - i, e, n) for i, char in enumerate(plain_text)]
        # Return the array of bytes
        return cipher

    def decrypt(self, private_key, cipher_text):
        # Unpack the key into its components
        d, n = private_key
        # Generate the plaintext based on the ciphertext and key using a^b mod m
        plain = [chr(pow(char, d, n) + i) for i, char in enumerate(ciphertext)]
        # Return the array of bytes as a string
        return ''.join(plain)


instance = RSAEncryption()
public, private = instance.generate_keypair()
print("Public key: " + str(public) + "\nPrivate key: " + str(private))

ciphertext = instance.encrypt(public, "Hello, world!")
print("Cipher text: " + str(ciphertext))

plaintext = instance.decrypt(private, ciphertext)
print("Plain text: " + str(plaintext))
