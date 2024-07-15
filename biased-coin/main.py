import numpy as np
import matplotlib.pyplot as plt
import rcparams
from modules.coin import coin

n_trials = 10000
n_max_flips = 500

p_heads_list = np.linspace(0.01, 0.999, 50)
flips_till_heads = np.zeros(len(p_heads_list))

with open('data/flips_till_heads.txt', 'w') as f:
    f.write("#p \t flips_till_heads\n")

with open('data/flips_till_heads.txt', 'a') as f:
    for p_i, p in enumerate(p_heads_list):
        percent_complete = p_i / len(p_heads_list) * 100
        if p_i % 10 == 0:
            print("Percent complete: {:.2f}%".format(percent_complete))
        for t_i, t in enumerate(range(n_trials)):
            c = coin(p)
            heads_flipped = False
            while not heads_flipped:
                r = c.flip()
                if r == 'H':
                    heads_flipped = True
                    flips_till_heads[p_i] += c.get_times_flipped()
                if c.get_times_flipped() > n_max_flips:
                    break
            c.reset()
        flips_till_heads[p_i] /= n_trials
        f.write("{:.5f} \t {:.5f}\n".format(p, flips_till_heads[p_i]))
        f.flush()
        