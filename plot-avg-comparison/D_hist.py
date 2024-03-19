import numpy as np
import matplotlib.pyplot as plt

D_list = np.loadtxt('data/D_list.txt')

mean = np.mean(D_list)
std = np.std(D_list)
trials = len(D_list)

plt.figure(tight_layout=True)

plt.hist(D_list, bins=20, color='b', edgecolor='k', alpha=1.0, rwidth=0.9, label='Trials = {}'.format(trials))
plt.axvline(mean, color='r', linestyle='dashed', linewidth=2, label=r'$\langle D \rangle$')
plt.xlabel(r'$D$', fontsize=18)
plt.ylabel('Frequency', fontsize=18)
plt.title(r'Trials = {}, $\langle D \rangle$ = {:.4f}, $\sigma$ = {:.4f}'.format(trials, mean, std), fontsize=18)
plt.legend()
plt.savefig('plots/D_hist.pdf')