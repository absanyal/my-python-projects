from matplotlib import axis
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import modules.parameters as prm

t, x, y, z = np.loadtxt('data/pos.txt', unpack=True)

# t = t[:100]

print(len(t))

shifts = np.arange(int(len(t)))
msd = np.zeros(shifts.size)

for i, shift in enumerate(shifts):
    dx = x[:-shift if shift else None] - x[shift:]
    dy = y[:-shift if shift else None] - y[shift:]
    dz = z[:-shift if shift else None] - z[shift:]
    sqdist = np.square(dx) + np.square(dy) + np.square(dz)
    msd[i] = np.mean(sqdist)


with open('data/sampled_muhung.txt', 'w') as file:
    file.write("# t \t <ds^2>\n")
    for i in range(len(t)):
        file.write("{} \t {}\n".format(t[i], msd[i]))

def f(x, m, c):
    return m*x + c

fit_params, fit_cov = curve_fit(f, t, msd)

D = fit_params[0]/(prm.dimension*2)

print('Diffusion coefficient: D = {:.4e}'.format(D))
print('or, approximately D = {:.4f}'.format(D))

fitline = f(t, *fit_params)

plt.figure(tight_layout=True)
plt.plot(t, msd, 'k-', label='Data')
plt.plot(t, fitline, 'r--', label='Fit')
plt.xlabel(r'$t/\tau$', fontsize=18)
plt.ylabel(r'$\langle \Delta s^2 \rangle$', fontsize=18)
plt.legend(fontsize=14)
plt.title('D = {:.4f}'.format(D), fontsize=18)

plt.savefig('plots/sampled_muhung.pdf')
