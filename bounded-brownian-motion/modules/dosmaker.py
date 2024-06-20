import numpy as np
from numpy import pi


def lorentzian(x, x0, gamma):
    return (1/pi) * ((gamma / 2) / ((x - x0)**2 + (gamma / 2)**2))

def make_dos(w_list, epsilon_list, gamma):
    dos = np.zeros_like(w_list)
    for e0 in epsilon_list:
        dos += lorentzian(w_list, e0, gamma)
    dos /= len(epsilon_list)
    
    return dos