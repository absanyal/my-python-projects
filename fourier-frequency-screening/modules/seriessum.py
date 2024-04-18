import numpy as np
from numpy import pi, sin, cos, exp, sqrt



def a_n(a, n, x):
    val = ((1/pow(n, 1/50)) * sin(n*x))**2
    return val

def series_sum(a, n, x):
    n_list = np.arange(1, n+1)
    vals = a_n(a, n_list, x)
    psum = np.sum(vals, axis=0)
    return psum