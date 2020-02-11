from Gates import hadamard
from util.ConsoleMessenger import print_info
from QubitRegister import QubitRegister
from QuantumModularExponentiation import quantum_modular_exponentiation
from QuantumFourierTransform import quantum_fourier_transform
from classical.ContinuedFractions import continued_fractions


def find_period(a, N):
    number_bit_length = N.bit_length()

    input_qubits = (2 * number_bit_length) - 1
    input_qubits += 1 if ((1 << input_qubits) < (N * N)) else 0

    q = 1 << input_qubits

    print_info("Finding Period...")
    print_info("Q = " + str(q) + "\ta = " + str(a))

    input_register = QubitRegister(input_qubits)
    hadamard_input_register = QubitRegister(input_qubits)
    qft_input_register = QubitRegister(input_qubits)
    output_register = QubitRegister(input_qubits)

    print_info("Qubit registers created.")
    print_info("Performing Hadamard gate on input register.")

    input_register.map(hadamard_input_register, lambda x: hadamard(x, q), False)

    print_info("Hadamard performed.")
    print_info("Performing modular exponentiation")

    hadamard_input_register.map(output_register, lambda x: quantum_modular_exponentiation(a, x, N), False)

    print_info("Modular exponentiation performed.")
    print_info("Performing QFT.")

    hadamard_input_register.map(qft_input_register, lambda x: quantum_fourier_transform(x, q), False)
    input_register.propagate()

    print_info("Performed QFT")
    print_info("Measuring output qubit register.")

    y = output_register.measure()

    print_info("Output register measurement = " + str(y))
    print_info("Measuring QFT register.")

    x = qft_input_register.measure()

    print_info("QFT register measurement = " + str(x))

    if x is None:
        return None  # No periodicity so no period to find.

    print_info("Using continued fractions to find the period.")

    r_period = continued_fractions(x, q, N)

    print_info("Found period = " + str(r_period))

    return r_period
