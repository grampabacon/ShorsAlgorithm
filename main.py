import argparse
import math
import random
import util.ConsoleMessenger as cm

from classical.ModularExponentiation import modular_exponentiation
from quantum.PeriodFinder import find_period
from util.ConsoleMessenger import print_info
from classical.GreatestCommonDivisor import greatest_common_divisor

# Disallow running the algorithm with too long a number that would take too long to compute TODO: Determine value
BIT_MAXIMUM = 20


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
# Console Input #
#################
def parse_args():
    parser = argparse.ArgumentParser(description='Simulate Shor\'s algorithm for N.')
    parser.add_argument('-a', '--attempts', type=int, default=20, help='Number of quantum attempts to perform')
    parser.add_argument('-n', '--neighborhood', type=float, default=0.01, help='Neighborhood size for checking candidates (as percentage of N)')
    parser.add_argument('-p', '--periods', type=int, default=2, help='Number of periods to get before determining least common multiple')
    parser.add_argument('-v', '--verbose', type=bool, default=True, help='Verbose')
    parser.add_argument('N', type=int, help='The integer to factor')
    return parser.parse_args()


#############
# Algorithm #
#############
def pick_a(N):
    a = math.floor((random.random() * (N - 1)) + 0.5)
    return a


def check_candidates(a, period, N, neighbourhood):
    if period is None:
        return None

    # Check multiples
    for i in range(1, neighbourhood + 2):
        _r = i * period
        if modular_exponentiation(a, a, N) == modular_exponentiation(a, a + _r, N):
            return _r

    # Check lower neighbourhood bound
    for j in range(period - neighbourhood, period):
        if modular_exponentiation(a, a, N) == modular_exponentiation(a, a + j, N):
            return j

    # Check upper neighbourhood bound
    for k in range(period + 1, period + neighbourhood + 1):
        if modular_exponentiation(a, a, N) == modular_exponentiation(a, a + k, N):
            return k

    return None


def run_shors(N, attempts=1, neighbourhood=0.0, num_periods=1):
    """
    Runs the classical implementation of Shors algorithm and returns the found prime factors.

    :param N: The number to factorise.
    :param attempts: The number of times to run the function per test. Default = 1.
    :param neighbourhood: The range of values to check around the output qubit register, as a % of N. Default = 0.0.
    :param num_periods: The number of successful tests of the function required before the greatest common divisor of the results is found. Default = 1.
    """
    if N.bit_length() > BIT_MAXIMUM or N < 3:
        return False

    periods = []
    neighbourhood = math.floor(N * neighbourhood) + 1

    print_info("N = " + str(N))
    print_info("Neighborhood = " + str(neighbourhood))
    print_info("Number of periods = " + str(num_periods))

    for attempt in range(attempts):
        print_info("\nAttempt " + str(attempt))

        a = pick_a(N)
        while a < 2:
            a = pick_a(N)

        divisor = greatest_common_divisor(a, N)
        if divisor > 1:
            print_info("Found factor classically, retry.")
            continue

        period = find_period(a, N)

        print_info("Checking candidate period, nearby values, and multiples")

        period = check_candidates(a, period, N, neighbourhood)

        if period is None:
            print_info("No period found, retry.")
            continue

        if (period % 2) != 0:
            print_info("Period was odd, retry.")
            continue

        divisor = modular_exponentiation(a, period // 2, N)
        if period == 0 or divisor == (N - 1):
            print_info("Period was trivial, retry.")
            continue

        print_info("Found period = " + str(period))

        periods.append(period)
        if len(periods) < num_periods:
            continue

        print_info("\nFinding greatest common divisor of found periods.")

        period = 1
        for r in periods:
            divisor = greatest_common_divisor(r, period)
            period = (period * r) // divisor

        b = modular_exponentiation(a, period // 2, N)
        return [greatest_common_divisor(N, b + 1), greatest_common_divisor(N, b - 1)]

    return None


def main():
    args = parse_args()

    if args.verbose:
        cm.print_info = cm.print_verbose
    else:
        cm.print_info = cm.print_none

    factors = run_shors(args.N, args.attempts, args.neighborhood, args.periods)
    if factors is not None:
        # print("Factors:\t" + str(factors[0]) + ", " + str(factors[1]))
        print("Factors:\t" + str(factors).strip("[]"))


print(run_shors(35, 20, 0.2, 2))
