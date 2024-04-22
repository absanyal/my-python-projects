from matplotlib.patches import bbox_artist
import numpy as np
import matplotlib.pyplot as plt

# Load data
t, fpd = np.loadtxt("data/firstpassage.dat", unpack=True)

info = np.loadtxt("data/info.dat", unpack=True)
D = info[0]
dt = info[1]
n_trials = info[2]
n_iters = info[3]
total_time = info[4]
initial_angle = info[5]
target_angle = info[6]

req_frac = 0.97

cdf = np.zeros(len(fpd))

for i in range(len(fpd)):
    cdf[i] = np.trapz(fpd[:i], t[:i])

for i in range(len(cdf)):
    if cdf[i] >= req_frac:
        print("{:.2f}% of the probability mass is reached at t={:.4f}".format(req_frac * 100, t[i]))
        print("Probability mass: {:.4f}".format(cdf[i]))
        break

plt.figure(tight_layout=True, figsize=(6, 4))

plt.plot(t, cdf, color="blue", label="CDF")
plt.plot(t, fpd, color="red", label="PDF")
plt.axvline(t[i], color="green", label=r"$t = {:.2f}$".format(t[i]), linestyle="--")
plt.axhline(req_frac, color="green", label=r"$P = {:.2f}$".format(req_frac), linestyle="--")
plt.axhline(1.0, color="black", linestyle="--")

plt.xlabel(r'$t/\tau$', fontsize=18)
plt.ylabel("Probability", fontsize=18)

plt.legend(loc="upper left", fontsize=12)

plt.title(r"$D = {:.4f}$    $\theta = {:.2f}\degree$".format(D, initial_angle), fontsize=18)

plt.ylim(bottom=0)
plt.xlim(left=0, right=max(t))

plt.savefig("plots/cdf.pdf")