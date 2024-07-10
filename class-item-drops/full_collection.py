import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 14
mpl.rcParams['axes.titlesize'] = 20

n_trials = 100000

tries_to_full_collection = []

fig, ax = plt.subplots(1, 2, figsize=(10, 5), tight_layout=True)

for t_i in range(n_trials):
    
    if t_i % 1000 == 0:
        print("Trial {} of {}".format(t_i, n_trials))
    
    collection = np.zeros((8, 8))
    full_collection = False
    tries_to_full_collection_this_trial = 0
    while not full_collection:
        perk1 = np.random.randint(0, 8)
        perk2 = np.random.randint(0, 8)
        collection[perk1, perk2] = 1
        tries_to_full_collection_this_trial += 1
        if np.sum(collection) == 64:
            full_collection = True
            tries_to_full_collection.append(tries_to_full_collection_this_trial)
    
    mean_tries_to_full_collection = np.mean(tries_to_full_collection)
    
    if t_i % 1000 == 0:
        ax[0].cla()
        ax[0].hist(tries_to_full_collection[:t_i], bins='auto', color='blue', rwidth=0.85, density=True, histtype='step')
        ax[0].set_xlabel("Tries to complete collection")
        ax[0].set_ylabel("Frequency")
        ax[0].set_title("PDF")
        ax[0].grid()
        ax[0].axvline(mean_tries_to_full_collection, color='red', linestyle='--', label="Mean: {:.2f}".format(mean_tries_to_full_collection))
        ax[0].legend()
        ax[0].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        
        ax[1].cla()
        ax[1].hist(tries_to_full_collection[:t_i], bins='auto', color='blue', rwidth=0.85, density=True, histtype='step', cumulative=True)
        ax[1].set_xlabel("Tries to complete collection")
        ax[1].set_ylabel("Probability")
        ax[1].set_title("CDF")
        ax[1].grid()
        ax[1].axvline(mean_tries_to_full_collection, color='red', linestyle='--', label="Mean: {:.2f}".format(mean_tries_to_full_collection))
        ax[1].legend()
        ax[1].ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        
        plt.savefig("full_collection.png")
            
            
