import numpy as np
from numpy import pi, sqrt, exp


def reflective_soln(x, x0, D, t):
    term1 = exp(- (x - x0)**2 / (4 * D * t))
    term2 = exp(- (x + x0)**2 / (4 * D * t))
    c = 1 / (2 * sqrt(4 * pi * D * t))
    return c * (term1 + term2)


def adsorptive_soln(x, x0, D, t):
    term1 = exp(- (x - x0)**2 / (4 * D * t))
    term2 = exp(- (x + x0)**2 / (4 * D * t))
    c = 1 / (sqrt(4 * pi * D * t))
    return c * (term1 - term2)
