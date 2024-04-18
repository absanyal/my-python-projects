import numpy as np
from numpy import sqrt, log10, sin, cos, exp, pi


class geneticf:
    def __init__(self, params):
        self.params = params

    def value(self, x):
        y = 0
        for i in range(len(self.params)):
            a = self.params[i]
            y += a * x**i
        return y

    def set_params(self, params):
        self.params = params

    def get_params(self):
        return self.params
