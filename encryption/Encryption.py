import math
import numpy as np


class Encryption:
    e = 5
    p = 5
    q = 7

    def productofprimes(self, p, q):
        N = p * q
        return N

    def relative_prime(self):
        z = (self.p - 1) * (self.q - 1)
        return z

    def derived_number(self):

        if self.e < 1:
            raise ValueError('Derived number must be an integer')
        if self.e > self.productofprimes(5, 7):
            raise ValueError('e must not be greater than N')
        if self.relative_prime() % self.e == 0:
            raise ValueError('1 must be the only common factor shared by both e and z')
        else:
            return self.e

    # The first half of the code is to check if the input variables p,q, and e can be used in the encryption scheme. The public key is formed by the two numbers N and e.
    def privatekey(self):
        self.e = self.e % self.relative_prime()
        for x in range(1, self.productofprimes(5, 7)):
            if (self.e * x) % self.relative_prime() == 1:
                print(x)
        return 1

    # This function creates one part of the private key, which is used to decrypt the message. The private key is formed from the numbers N and x.
    def encryption(self, list_message):
        r = []
        for b in list_message:
            c = (b ** self.derived_number()) % self.productofprimes(5, 7)
            r.append(c)
        return r

    # This function uses numbers to encrypt messages. In this case, numbers correspond to letters, a=1,b=2,c=3 etc.
    def decryption(self, encrypted_list):
        x = 5
        t = []
        for y in encrypted_list:
            f = (y ** x % self.productofprimes(5, 7))
            t.append(f)
        return t


# instance = Encryption()
# instance.encryption()
# instance.privatekey()
# instance.decryption()
