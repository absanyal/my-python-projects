import numpy as np
import matplotlib.pyplot as plt

n_sample = 1000000

drops_required = 1
drop_chance = 0.25

tries_list=[]

for n in range(n_sample):
    drops_obtained = 0
    attempts = 0
    while (drops_obtained < drops_required):
        attempts += 1
        r = np.random.uniform(0, 1)
        if (r < drop_chance):
            drops_obtained += 1
    tries_list.append(attempts)

plt.hist(tries_list, bins=20)
plt.show()

print("Average:", np.mean(tries_list))
print("Std Dev:", np.std(tries_list))
print("Min:", np.min(tries_list))
print("Max:", np.max(tries_list))