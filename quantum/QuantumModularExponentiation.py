from classical import ModularExponentiation
from quantum.Mapping import QuantumMap


# Quantum Modular Exponentiation
def quantum_modular_exponentiation(a, exp, mod):
    state = ModularExponentiation.modular_exponentiation(a, exp, mod)
    amplitude = complex(1.0)
    return [QuantumMap(state, amplitude)]
