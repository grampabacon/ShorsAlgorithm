# Find greatest common divisor
def greatest_common_divisor(a, b):
    while b > 0:
        a, b = b, a % b
    return a


# Extended Euclidean Algorithm
def extended_gcd(a, b):
    fractions = []
    while b != 0:
        fractions.append(a // b)
        a = a % b
        a, b = b, a
    return fractions
