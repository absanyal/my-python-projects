from cProfile import label
from turtle import up
import numpy as np
import matplotlib.pyplot as plt
from modules.dos import dos_maker

num_connected_list = np.loadtxt("data/connected_data.txt")
chain_length, T = np.loadtxt("data/chain_info.txt", unpack=True)

draw_hist = 0

# For DOS plot
n_x_axis = 1000
gamma = 0.1
buffer = 2

print("Chain length:", chain_length)
print("Temperature: {} K".format(T))

avg_connections = np.mean(num_connected_list)
connectedness = avg_connections / chain_length
std = np.std(num_connected_list)

bunching_constant = 1

if (bunching_constant < 1):
    bunching_constant = 1

print("Avg. connected sites: {:.2f}".format(avg_connections))
print("Standard deviation: {:.2f}".format(std))
print("Avg. connectedness: {:.2f}".format(connectedness))


plt.figure(tight_layout=True)
plt.xlabel("Number of connected sites", fontsize=18)
plt.ylabel("Frequency", fontsize=18)
bins_list = np.arange(0, chain_length + 1, int(bunching_constant))

if draw_hist:
    plt.hist(num_connected_list, bins=bins_list, color="blue", edgecolor="none", rwidth=0.75, density=True, label="Frequency")
else:
    x_vals = np.linspace(0 - buffer, chain_length + 1 + buffer, n_x_axis)
    dos_vals = dos_maker(x_vals, num_connected_list, gamma)
    plt.plot(x_vals, dos_vals, color="blue", linewidth=1, label="Frequency")

plt.axvline(avg_connections, color="red", linestyle="dashed", linewidth=1, label=r'$\langle n \rangle = {} \pm {}$'.format(round(avg_connections, 2), round(std, 2)))
plt.legend(fontsize=12)
plt.ylim(bottom=0)
plt.title(r"Avg. connectedness: {:.2f} at {:.2f} K".format(connectedness, T), fontsize=18)
plt.savefig("plots/chain_hist.pdf")