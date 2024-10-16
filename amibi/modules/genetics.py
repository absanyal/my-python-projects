import numpy as np
from modules.amibi import amibi

def make_gamete(a:amibi):
    s1 = a.DNA1
    s2 = a.DNA2
    crossover_point = np.random.randint(2, len(s1))
    s_new = s1[:crossover_point] + s2[crossover_point:]
    return s_new

def reproduce(a1:amibi, a2:amibi):
    s1 = make_gamete(a1)
    s2 = make_gamete(a2)
    child = amibi(s1, s2)
    return child

def clone(a:amibi):
    s1 = a.DNA1
    s2 = a.DNA2
    child = amibi(s1, s2)
    return child

