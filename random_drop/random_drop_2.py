import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm

n_sample = 100000

n_advantage = 14

drops_required = 1
drop_chance = 0.05
first_timers = 0.0

tries_list = []

for n in tqdm(range(n_sample)):
    drops_obtained = 0
    attempts = 0
    while (drops_obtained < drops_required):
        attempts += 1
        r_total = np.random.uniform(0, 1, n_advantage)
        r = np.min(r_total)
        if (r < drop_chance):
            drops_obtained += 1
    tries_list.append(attempts)
    if (attempts == 1):
        first_timers += 1

plt.hist(tries_list, bins=20, density=True)
# plt.show()

print("Average:", np.mean(tries_list))
print("Std Dev:", np.std(tries_list))
print("Min:", np.min(tries_list))
print("Max:", np.max(tries_list))
print("First timers:", first_timers, ",", (first_timers * 100/n_sample), "%")
