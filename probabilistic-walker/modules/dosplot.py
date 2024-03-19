import numpy as np

def lorentzian(x, x0, gamma):
    g = gamma / 2
    return g / (np.pi * (g**2 + (x - x0)**2))

def dosplot(w_list, spectrum, gamma):
    dos = np.zeros_like(w_list)
    for e0 in spectrum:
        dos += lorentzian(w_list, e0, gamma)
    dos /= len(spectrum)
    return dos
    
    