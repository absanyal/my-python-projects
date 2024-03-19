from cProfile import label
from turtle import title
from matplotlib import tight_layout
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation


def flip_spin(lattice, T, J1, J2, J3, H):
    L = lattice.shape[0]
    i, j = np.random.randint(0, L, 2)
    dE = 2 * J1 * lattice[i, j] * (lattice[(i+1) % L, j] + lattice[i-1, j] +
                                   lattice[i, (j+1) % L] + lattice[i, j-1]) - 2 * H * lattice[i, j] + 2 * J2 * lattice[i, j] * (lattice[(i+2) % L, j] + lattice[i-2, j] + lattice[i, (j+2) % L] + lattice[i, -2]) + 2 * J3 * lattice[i, j] * (lattice[(i+1) % L, (j+1) % L] + lattice[i-1, j-1] + lattice[i-1, (j+1) % L] + lattice[(i+1) % L, j-1])

    if dE < 0 or np.random.rand() < np.exp(-dE/T):
        lattice[i, j] *= -1


def MC_sweep(lattice, T, J1, J2, J3, H):
    L = lattice.shape[0]
    for _ in range(L**2):
        flip_spin(lattice, T, J1, J2, J3, H)


L = 20
lattice = np.random.choice([-1, 1], size=(L, L))

H = 0.0
J1 = 0.0
J2 = 1.0
J3 = -1.0

num_sweeps_per_T = 100

T_initial = 5.0
T_final = 1.0

T = T_initial
T_list = [T_initial]
while T > T_final:
    if (T > 2.3):
        T_step = 0.1
    elif (T > 1.5):
        T_step = 0.05
    elif (T > 0.5):
        T_step = 0.02
    else:
        T_step = 0.01
    T -= T_step
    T_list.append(T)

T_list = np.array(T_list)

frames_list = []

fig = plt.figure(tight_layout=False)
ax = fig.add_subplot(111)

for T in T_list:
    print("T = {:.2f}".format(T))
    for _ in range(num_sweeps_per_T):
        ttl = plt.text(0.5, 1.01, "T = {:.2f}".format(T), horizontalalignment='center',
                       verticalalignment='bottom', fontsize=15, color='black', transform=ax.transAxes)
        MC_sweep(lattice, T, J1, J2, J3, H)
        im = plt.imshow(lattice, animated=True,
                        cmap='gray', interpolation='none')
        frames_list.append([im, ttl])

ani = ArtistAnimation(fig, frames_list, interval=1000/60, blit=False)
plt.show()
