import numpy as np
import matplotlib.pyplot as plt

# Load data
iter, time = np.loadtxt("data/timehist.dat", unpack=True)

info = np.loadtxt("data/info.dat", unpack=True)
D = info[0]
dt = info[1]
n_trials = info[2]
n_iters = info[3]
total_time = info[4]
initial_angle = info[5]
target_angle = info[6]

# Plot histogram

bins_list = np.arange(0, max(time), 1.0)
# bins_list = 'auto'

plt.figure(tight_layout=True, figsize=(6, 4))

plt.hist(time, bins=bins_list, density=True, color="blue", edgecolor="None", rwidth=0.7, label="Data", align="mid", alpha=0.5, histtype="bar")
plt.xlabel(r'$t/\tau$', fontsize=18)
plt.ylabel("Frequency", fontsize=18)

plt.axvline(np.mean(time), color="blue", label="Mean: {:.4f}".format(np.mean(time)), linestyle="--")

t, fpd = np.loadtxt("data/firstpassage.dat", unpack=True)

plt.plot(t, fpd, color="red", label = "First Passage Distribution")

theory_mean = np.trapz(t*fpd, t)

plt.axvline(theory_mean, color="red", label="Theoretical Mean: {:.4f}".format(theory_mean), linestyle="--")

plt.xlim(left = -1)
# plt.xlim(left = -1, right=50)
plt.ylim(bottom=0)

plt.title(r"$D = {:.4f}$    $\theta = {:.2f}\degree$".format(D, initial_angle), fontsize=18)

plt.legend()
plt.savefig("plots/hist.pdf")