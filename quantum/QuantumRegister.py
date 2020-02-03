import math

from quantum.QuantumState import QuantumState


class QuantumRegister:
    """

    """

    def __init__(self, numBits):
        self.numBits = numBits
        self.numStates = 1 << numBits
        self.entangled = []
        self.states = [QuantumState(complex(0.0), self) for x in range(self.numStates)]
        self.states[0].amplitude = complex(1.0)

    """
    
    """
    def set_propagate(self, register=None):
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
    """
    def SetMap(self, register, mapping, propagate=True):
        self.entangled.append(register)
        register.entangled.append(self)
        mapTensorX = {}
        mapTensorY = {}
        for x in range(self.numStates):
            mapTensorX[x] = {}
            codomain = mapping(x)
            for element in codomain:
                y = element.state
                mapTensorX[x][y] = element
                try:
                    mapTensorY[y][x] = element
                except KeyError:
                    mapTensorY[y] = {x: element}

        def SetNormalize(tensor, p=False):
            lSqrt = math.sqrt
            for vectors in tensor.values():
                sumProb = 0.0
                for element in vectors.values():
                    amplitude = element.amplitude
                    sumProb += (amplitude * amplitude.conjugate()).real
                normalized = lSqrt(sumProb)
                for element in vectors.values():
                    element.amplitude = element.amplitude / normalized

        SetNormalize(mapTensorX)
        SetNormalize(mapTensorY, True)
        for x, yStates in mapTensorX.items():
            for y, element in yStates.items():
                amplitude = element.amplitude
                toState = register.states[y]
                fromState = self.states[x]
                toState.entangle(fromState, amplitude)
                fromState.entangle(toState, amplitude.conjugate())
        if propagate:
            register.propagate(self)
