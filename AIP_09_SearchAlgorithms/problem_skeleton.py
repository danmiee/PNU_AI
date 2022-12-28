import random
import math


class Problem:
    def __init__(self):
        self._solution = None
        self._value = 0
        self._numEval = 0

    def setVariables(self):
        pass
    
    def randomInit(self):
        pass

    def evaluate(self):
        pass

    def mutants(self):
        pass

    def randomMutant(self, current):
        pass

    def describe(self):
        pass

    def storeResult(self, solution, value):
        self._solution = solution
        self._value = value

    def report(self):
        print()
        print("Total number of evaluations: {0:,}".format(self._numEval))


class Numeric(Problem):
    def __init__(self):

    
    def setVariables(self):

    def getDelta(self):

    def randomInit(self): # Return a random initial point as a list

    def evaluate(self, current):

    def mutants(self, current):

    def mutate(self, current, i, d): ## Mutate i-th of 'current' if legal

    def randomMutant(self, current):

    def describe(self):

    def report(self):

    def coordinate(self):
