class QuantumMap:
    """
    Quantum map which assigns a probability amplitude to a given state.

    :param state - state with probability of measurement
    :param amplitude - probability of finding state when making a measurement
    """
    def __init__(self, state, amplitude):
        self.state = state
        self.amplitude = amplitude
