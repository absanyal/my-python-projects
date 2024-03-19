import numpy as np
import matplotlib.pyplot as plt
import modules.brownian as brn
from scipy.optimize import curve_fit

def linear(x, m, c):
    return m * x + c

dimension = 2

t_list, dist_sq = np.loadtxt('data/distance.dat', unpack=True)

t_fit = np.linspace(min(t_list), max(t_list), 1000)

popt, pcov = curve_fit(linear, t_list, dist_sq)

y_fit = linear(t_fit, *popt)

plt.figure(tight_layout=True)
plt.plot(t_list, dist_sq, label=r'$\langle r^2 \rangle$', color='r', lw=2)
plt.plot(t_fit, y_fit, label=r'Fit: $\langle r^2 \rangle = {:.2f}t + {:.2f}$'.format(popt[0], popt[1]), color='b', lw=1.5, ls=':')

print('D = {:.2f}'.format(popt[0] / (dimension * 2)))

plt.xlabel(r'$t/\tau$', fontsize=18)
plt.ylabel(r'$\langle r^2 \rangle$', fontsize=18)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(fontsize=12)
plt.savefig('plots/distance.pdf')