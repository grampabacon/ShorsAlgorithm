import argparse
import math

from quantum.Mapping import QuantumMap
from quantum.QubitRegister import QubitRegister

# Disallow running the algorithm with too long a number that would take too long to compute TODO: Determine value
BIT_MAXIMUM = 20


#######################
# Classical Functions #
#######################
def bit_count(x):
    sum_bits = 0
    while x > 0:
        sum_bits += x & 1
        x >>= 1

    return sum_bits

# Find greatest common divisor
def greatest_common_divisor(a, b):
    if b > a:
        a, b = b, a
    while b > 0:
        a = a % b
        a, b = b, a
    return a


def

#########################
# Quantum Data Printing #
#########################
def print_entangled_states(register):
    print_info("Entangled States: " + str(register.entangled))


def print_amplitudes(register):
    amplitudes = register.get_amplitudes()
    for x, amplitude in enumerate(amplitudes):
        print_info('State #' + str(x) + '\'s amplitude: ' + str(amplitude))


#################
# Quantum Gates #
#################

"""
q: input quantum bit.
"""
def hadamard(x, q):
    codomain = []
    for y in range(q):
        amplitude = complex(pow(-1.0, bit_count(x & y) & 1))
        codomain.append(QuantumMap(y, amplitude))

    return codomain


def quantum_modular_exponentiation(a, exp, mod):
    state = modular_exponentiation(a, exp, mod)
    amplitude = complex(1.0)

    return [QuantumMap(state, amplitude)]


def quantum_fourier_transform(x, q):
    float_q = float(q)
    k = -2.0 * math.pi
    codomain = []

    for y in range(q):
        angle = (k * float((x * y) % q)) / float_q
        amplitude = complex(math.cos(angle), math.sin(angle))
        codomain.append(QuantumMap(y, amplitude))

    return codomain


def find_period(a, N):
    number_bit_length = N.bit_length()

    input_qubits = (2 * number_bit_length) - 1
    input_qubits += 1 if ((1 << input_qubits) < (N * N)) else 0

    q = 1 << input_qubits

    print_info("Finding the period of the state...")
    print_info("Q = " + str(q) + "\ta = " + str(a))

    input_register = QubitRegister(input_qubits)
    hadamard_input_register = QubitRegister(input_qubits)
    qft_input_register = QubitRegister(input_qubits)
    output_register = QubitRegister(input_qubits)

    print_info("Registers created.")
    print_info("Performing Hadamard gate on input register.")

    input_register.map(hadamard_input_register, lambda x: hadamard(x, q), False)

    print_info("Hadamard performed.")
    print_info("Hadamard performed.")


###############################
# Command Line Functionality. #
###############################
def print_none(string):
    pass


def print_verbose(string):
    print(string)


print_info = print_none


def parseArgs():
    parser = argparse.ArgumentParser(description='Simulate Shor\'s algorithm for N.')
    parser.add_argument('-a', '--attempts', type=int, default=20, help='Number of quantum attempts to perform')
    parser.add_argument('-n', '--neighborhood', type=float, default=0.01, help='Neighborhood size for checking candidates (as percentage of N)')
    parser.add_argument('-p', '--periods', type=int, default=2, help='Number of periods to get before determining least common multiple')
    parser.add_argument('-v', '--verbose', type=bool, default=True, help='Verbose')
    parser.add_argument('N', type=int, help='The integer to factor')
    return parser.parse_args()


def main():
    args = parseArgs()

    global printInfo
    if args.verbose:
        printInfo = print_verbose
    else:
        printInfo = print_none

    factors = shors(args.N, args.attempts, args.neighborhood, args.periods)
    if factors is not None:
        print("Factors:\t" + str(factors[0]) + ", " + str(factors[1]))
