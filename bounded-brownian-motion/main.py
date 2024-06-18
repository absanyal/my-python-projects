import numpy as np
import matplotlib.pyplot as plt

from modules.walker import walker
from modules.wall import wall

# Define the number of trials and iterations
num_trials = 50000
num_iters = 1000

# Define the wall
xmin = -30
xmax = 30

ymin = -30
ymax = 30

zmin = -30
zmax = 30

this_wall = wall(xmin, xmax, ymin, ymax, zmin, zmax)

# Define the walker
Dx = 1.0
Dy = 1.0
Dz = 1.0
D = np.array([Dx, Dy, Dz])

x0 = 0
y0 = 0
z0 = 0

dt = 0.02

this_walker = walker(D, x0, y0, z0, dt, this_wall)


final_x = np.zeros(num_trials)
final_y = np.zeros(num_trials)
final_z = np.zeros(num_trials)

bin_x = np.arange(xmin, xmax + 1, 1.0)
bin_y = np.arange(xmin, xmax + 1, 1.0)
bin_z = np.arange(xmin, xmax + 1, 1.0)

for trial in range(num_trials):

    this_walker.reset()
    for ti in range(num_iters):
        this_walker.step()

    final_x[trial] = this_walker.x
    final_y[trial] = this_walker.y
    final_z[trial] = this_walker.z

    if trial % 100 == 0 and trial > 0:

        print('Trial:', trial)

        fig, ax = plt.subplots(1, 3, figsize=(15, 5), tight_layout=True)

        ax[0].hist(final_x[:trial], bins=bin_x,
                   density=True, color='b', rwidth=0.8)
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('Density')
        ax[0].set_xlim(xmin, xmax)

        ax[1].hist(final_y[:trial], bins=bin_y,
                   density=True, color='b', rwidth=0.8)
        ax[1].set_xlabel('y')
        ax[1].set_ylabel('Density')
        ax[1].set_xlim(ymin, ymax)

        ax[2].hist(final_z[:trial], bins=bin_z,
                   density=True, color='b', rwidth=0.8)
        ax[2].set_xlabel('z')
        ax[2].set_ylabel('Density')
        ax[2].set_xlim(zmin, zmax)

        plt.savefig('histograms.png')

        plt.close()

        fig, ax = plt.subplots(1, 3, figsize=(15, 5), tight_layout=True)

        ax[0].scatter(final_x[:trial], final_y[:trial], s=5, c='b', alpha=0.2)
        ax[0].set_xlabel('x')
        ax[0].set_ylabel('y')
        ax[0].set_xlim(xmin, xmax)
        ax[0].set_ylim(ymin, ymax)
        ax[0].set_title('x - y projection')

        ax[1].scatter(final_x[:trial], final_z[:trial], s=5, c='b', alpha=0.2)
        ax[1].set_xlabel('x')
        ax[1].set_ylabel('z')
        ax[1].set_xlim(xmin, xmax)
        ax[1].set_ylim(zmin, zmax)
        ax[1].set_title('x - z projection')

        ax[2].scatter(final_y[:trial], final_z[:trial], s=5, c='b', alpha=0.2)
        ax[2].set_xlabel('y')
        ax[2].set_ylabel('z')
        ax[2].set_xlim(ymin, ymax)
        ax[2].set_ylim(zmin, zmax)
        ax[2].set_title('y - z projection')

        plt.savefig('finalpos.png')

        plt.close()
