import numpy as np
import matplotlib.pyplot as plt
from modules.firstpassage import firstpassageexact, firstpassage, wald
from numpy import pi

t = np.linspace(1e-3, 3, 2000)

fp = np.zeros_like(t)
fpexact = np.zeros_like(t)
wd = np.zeros_like(t)

theta_0 = 0

terms = 40

theta_0 = np.radians(theta_0)

plt.figure(tight_layout=True)

for i, tt in enumerate(t):
    fp[i] = firstpassage(tt, theta_0)
    fpexact[i] = firstpassageexact(tt, theta_0, terms)
    wd[i] = wald(tt, theta_0)
    
    plt.clf()
    plt.cla()

    if (i % 50 == 0 and i > 0):
        print(f'Plotting {i} of {len(t)}')
        plt.plot(t[:i], fp[:i], label='Approximation', color='red', linewidth=2)
        plt.plot(t[:i], fpexact[:i], label='Exact', linestyle='--', color='k')
        plt.plot(t[:i], wd[:i], label='Wald', linestyle='-', color='blue')
        plt.legend()
        
        plt.title(r"$\theta_0 = {:.2f} \degree$".format(np.degrees(theta_0)))
        
        plt.ylim(bottom=0)
        plt.xlim(left=0)
        
        # plt.yscale('log')

        plt.savefig('firstpassage.pdf')
    