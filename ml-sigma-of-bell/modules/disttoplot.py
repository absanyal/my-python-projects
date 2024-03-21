import numpy as np

def disttoplot(data, bins=100, density=True):
    plot = np.histogram(data, bins=bins, density=True)
    return plot[1][1:], plot[0]