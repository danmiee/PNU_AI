
class Setup:
    def __init__(self):
        self._aType = 0
        self._delta = 0.01     # Step size for axis-parallel mutation
        self._alpha = 0.01     # Update rate for gradient descent
        self._dx = 10 ** (-4)  # Increment for calculating derivative

    def setVariables(self, parameters):
        self._aType = parameters['aType']
        self._delta = parameters['delta']
        self._alpha = parameters['alpha']
        self._dx = parameters['dx']
    
    def getAType(self):
        return self._aType