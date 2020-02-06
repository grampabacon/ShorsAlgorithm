import math
import random

from quantum.QuantumState import QuantumState


class QubitRegister:
    """

    """
    def __init__(self, num_bits):
        self.numBits = num_bits
        self.numStates = 1 << num_bits
        self.entangled = []
        self.states = [QuantumState(complex(0.0), self) for x in range(self.numStates)]
        self.states[0].amplitude = complex(1.0)

    """
    
    """
    def propagate(self, register=None):
        if register is not None:
            for state in self.states:
                amplitude = complex(0.0)
                try:
                    entangles = state.entangled[register]
                    for entangle in entangles:
                        amplitude += entangle.state.amplitude * entangle.amplitude
                    state.amplitude = amplitude
                except KeyError:
                    state.amplitude = amplitude
        for register in self.entangled:
            if register is register:
                continue
            register.propagate(self)

    """
    This method sets the normalized tensorX and Y lists.
    Converts any mapping to a unitary tensor given each element follows
    v * v.conjugate() = 1
    """
    def map(self, register, mapping, propagate=True):
        self.entangled.append(register)
        register.entangled.append(self)

        # Create covariant / contravariant representations
        map_tensor_x = {}
        map_tensor_y = {}
        for x in range(self.numStates):
            map_tensor_x[x] = {}
            codomain = mapping(x)
            for element in codomain:
                y = element.state
                map_tensor_x[x][y] = element
                try:
                    map_tensor_y[y][x] = element
                except KeyError:
                    map_tensor_y[y] = {x: element}

        def normalise(tensor, p=False):
            l_sqrt = math.sqrt
            for vectors in tensor.values():
                sum_prob = 0.0
                for e in vectors.values():
                    amp = e.amplitude
                    sum_prob += (amp * amp.conjugate()).real
                normalized = l_sqrt(sum_prob)
                for e in vectors.values():
                    e.amplitude = e.amplitude / normalized

        normalise(map_tensor_x)
        normalise(map_tensor_y, True)
        for x, yStates in map_tensor_x.items():
            for y, element in yStates.items():
                amplitude = element.amplitude

                to_state = register.states[y]
                from_state = self.states[x]

                to_state.entangle(from_state, amplitude)
                from_state.entangle(to_state, amplitude.conjugate())
        if propagate:
            register.propagate(self)

    """
    Measure system and return the final state which has the highest probability.
    """
    def measure(self):
        measure = random.random()
        sum_probability = 0.0

        # Look for the state with highest probability.
        final_x_value = None
        final_state = None
        for x, state in enumerate(self.states):
            amplitude = state.amplitude
            sum_probability += (amplitude * amplitude.conjugate()).real

            if sum_probability > measure:
                final_state = state
                final_x_value = x
                break

        # If state is found, update the system. Collapse other states and set the chosen state as probability 1.
        if final_state is not None:
            for state in self.states:
                state.amplitude = complex(0.0)
            final_state.amplitude = complex(1.0)
            self.propagate()

        return final_x_value

    def get_entangled(self, register=None):
        entangled = 0
        for state in self.states:
            entangled += state.entangled(None)

        return entangled

    def get_amplitudes(self):
        amplitudes = []
        for state in self.states:
            amplitudes.append(state.amplitude)

        return amplitudes
