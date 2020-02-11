from Mapping import QuantumMap


def bit_count(x):
    sum_bits = 0
    while x > 0:
        sum_bits += x & 1
        x >>= 1

    return sum_bits


"""
q: input quantum bit.
"""


def hadamard(x, q):
    codomain = []
    for y in range(q):
        amplitude = complex(pow(-1.0, bit_count(x & y) & 1))
        codomain.append(QuantumMap(y, amplitude))

    return codomain
