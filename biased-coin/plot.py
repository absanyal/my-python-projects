import numpy as np
import matplotlib.pyplot as plt
import rcparams

p, flips = np.loadtxt('data/flips_till_heads.txt', unpack=True)

plt.plot(p, flips, color='black', linestyle='-')
plt.xlabel('p')
plt.ylabel('Average flips till heads')

plt.xlim(0, 1)
plt.ylim(bottom=0)

plt.savefig('plots/flips_till_heads.pdf')