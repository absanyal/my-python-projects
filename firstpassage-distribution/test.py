from turtle import title
import matplotlib
from networkx import stochastic_block_model
import numpy as np
import matplotlib.pyplot as plt
import modules.cdf as cdf
from modules.distributions import firstpassage, wald
from scipy.special import legendre
from matplotlib import rc, tight_layout
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import MultipleLocator
import scipy
from scipy.special import legendre
import numpy as np
from math import cos
import time
minorLocator1 = AutoMinorLocator()
minorLocator2 = AutoMinorLocator()


# Set the font
rc('font', family='serif')
rc('figure', figsize=(10, 6))
# rc('text', usetex=True)
rc('font', size=18)

t_list = np.linspace(0.001, 3, 1000)

color_list = list(matplotlib.colors.CSS4_COLORS.keys())

print(color_list)