import numpy as np
import matplotlib.pyplot as plt

a, b, c, x1, x2, xp1, xp2 = np.loadtxt('quadratic_results.txt', skiprows=1, unpack=True, usecols=(0, 1, 2, 3, 4, 5, 6))

fig, ax = plt.subplots(1, 2, figsize=(12, 6), tight_layout=True)

xt1 = np.linspace(min(x1), max(x1), 100)
xt2 = np.linspace(min(x2), max(x2), 100)

ax[0].scatter(x1, xp1, c='r', label='x1', s=10)
ax[0].plot(xt1, xt1, 'k--', label = "Truth line", linewidth=1.0)
ax[0].set_xlabel(r'True $x_1$', fontsize=18)
ax[0].set_ylabel(r'Predicted $x_1$', fontsize=18)
ax[0].set_title(r'$x_1$', fontsize=18)
ax[0].legend(fontsize=18)

ax[1].scatter(x2, xp2, c='b', label='x2', s=10)
ax[1].plot(xt2, xt2, 'k--', label = "Truth line", linewidth=1.0)
ax[1].set_xlabel(r'True $x_2$', fontsize=18)
ax[1].set_ylabel(r'Predicted $x_2$', fontsize=18)
ax[1].set_title(r'$x_2$', fontsize=18)
ax[1].legend(fontsize=18)

plt.savefig('quadratic_results.png')