from Mapping import QuantumMap


class QuantumState:
    """
    QuantumState class has methods related to describing a quantum state. Fundamental for quantum computing.

    :param amplitude - Probability of finding this state in a measurement.
    :param register - The qubit registry of the system.
    """
    def __init__(self, amplitude, register):
        self.amplitude = amplitude
        self.register = register
        self.entangled = {}

    """
    Set the state entangled to another.
    
    :param state - the state being entangled with.
    :param amplitude - probability of finding this state in the entanglement.
    """
    def entangle(self, state, amplitude):
        register = state.register
        entanglement = QuantumMap(state, amplitude)

        try:
            self.entangled[register].append(entanglement)
        except KeyError:
            self.entangled[register] = [entanglement]

    """
        Returns the length of entangled states list.

        :param register - the register of the state to find the length of. Default: None.
    """
    def get_entangled_states_length(self, register=None):
        entangled = 0
        if register is None:
            for states in self.entangled.values():
                entangled += len(states)
        else:
            entangled = len(self.entangled[register])
        return entangled
