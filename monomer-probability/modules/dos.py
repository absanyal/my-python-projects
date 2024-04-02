import numpy as np
from numpy import pi


def lorentzian(x, x0, gamma):
    return (1 / pi) * (gamma / 2) / ((x - x0) ** 2 + (gamma / 2) ** 2)

def dos_maker(x_vals, y_vals, gamma):
    dos = np.zeros_like(x_vals)
    
    norm = len(y_vals)
    
    for y in y_vals:
        dos += lorentzian(x_vals, y, gamma) / norm
    
    return dos
    