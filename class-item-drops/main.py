import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 14
mpl.rcParams['axes.titlesize'] = 20

drop_rate = 0.025

n_trials = 1000000

tries_till_consecutive_drops = []

consecutive_drops_has_happened = False

max_chests_opened = 50000

fig, ax = plt.subplots(1, 2, figsize=(10, 5), tight_layout=True)

for t_i in range(n_trials + 1):
    chests_opened = 0
    drop1 = 0
    drop2 = 0
    consecutive_drops_has_happened = False
    if t_i % 10000 == 0:
        print("Trial: {} / {}".format(t_i, n_trials))
    while not consecutive_drops_has_happened and chests_opened < max_chests_opened:
        drop2 = np.random.choice([0, 1], p=[1 - drop_rate, drop_rate])
        chests_opened += 1
        if drop1 == 1 and drop2 == 1:
            consecutive_drops_has_happened = True
            tries_till_consecutive_drops.append(chests_opened)
        else:
            drop1 = drop2
    
    mean_chests_opened = np.mean(tries_till_consecutive_drops)
    
    if t_i % 1000 == 0:
        ax[0].cla()
        ax[0].hist(tries_till_consecutive_drops, bins='auto', color='blue', rwidth=0.85, density = True, histtype='step')
        ax[0].set_title("PDF")
        ax[0].set_xlabel("Tries till consecutive drops")
        ax[0].set_ylabel("Frequency")
        ax[0].axvline(mean_chests_opened, color='red', linestyle='dashed', linewidth=2, label='Mean: {:.2f}'.format(mean_chests_opened))
        ax[0].grid()
        ax[0].legend()
        ax[0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        
        ax[1].cla()
        ax[1].hist(tries_till_consecutive_drops, bins='auto', color='blue', rwidth=0.85, cumulative = True, density = True, histtype='step')
        ax[1].set_title("CDF")
        ax[1].set_xlabel("Tries till consecutive drops")
        ax[1].set_ylabel("Probability")
        ax[1].grid()
        ax[1].axvline(mean_chests_opened, color='red', linestyle='dashed', linewidth=2, label='Mean: {:.2f}'.format(mean_chests_opened))
        ax[1].legend()
        ax[1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        
        plt.savefig("histogram.png")
        
            
    