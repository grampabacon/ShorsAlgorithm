import math
from Mapping import QuantumMap


def quantum_fourier_transform(x, q):
    float_q = float(q)
    k = -2.0 * math.pi
    codomain = []

    for y in range(q):
        angle = (k * float((x * y) % q)) / float_q
        amplitude = complex(math.cos(angle), math.sin(angle))
        codomain.append(QuantumMap(y, amplitude))

    return codomain
