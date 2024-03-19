import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('linker-near-surface-time.txt')

bins_list = np.arange(0, 50+1, 1)

plt.figure(tight_layout=True)
plt.hist(data, bins=bins_list, density=True, color='b', rwidth=0.8, align='mid')
plt.xlabel('Attached linkers', fontsize=18)
plt.ylabel('Probability', fontsize=18)
plt.savefig('linker-near-surface-plot.pdf')