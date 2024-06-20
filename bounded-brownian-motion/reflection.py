import numpy as np
import matplotlib.pyplot as plt
from modules.walker import walker
from modules.wall import wall

import matplotlib as mpl

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 16

# Define the number of trials and iterations
num_trials = 35000
num_iters = 1000

# Define the wall
xmin = -30
xmax = 30

ymin = -30
ymax = 30

zmin = -30
zmax = 30

this_wall = wall(xmin, xmax, ymin, ymax, zmin, zmax)

# Define the relective walker
distance_from_wall = 10.0

Dx = 1.0
Dy = 0.0
Dz = 0.0
D = np.array([Dx, Dy, Dz])

x0 = xmax - distance_from_wall
y0 = 0
z0 = 0

dt = 0.02

r_walker = walker(D, x0, y0, z0, dt, this_wall)

# Define the image walker 1
Dx = 1.0
Dy = 0.0
Dz = 0.0
D = np.array([Dx, Dy, Dz])

x0 = xmax - distance_from_wall
y0 = 0
z0 = 0

dt = 0.02

i_walker = walker(D, x0, y0, z0, dt, None)

# Define the image walker 2

Dx = 1.0
Dy = 0.0
Dz = 0.0
D = np.array([Dx, Dy, Dz])

x0 = xmax + distance_from_wall
y0 = 0
z0 = 0

dt = 0.02

i_walker2 = walker(D, x0, y0, z0, dt, None)

final_x_r = np.zeros(num_trials)

final_x_i1 = np.zeros(num_trials)
final_x_i2 = np.zeros(num_trials)

for trial in range(num_trials):

    r_walker.reset()
    i_walker.reset()
    i_walker2.reset()

    for ti in range(num_iters):

        r_walker.step()
        i_walker.step()
        i_walker2.step()

    final_x_r[trial] = r_walker.x

    final_x_i1[trial] = i_walker.x
    final_x_i2[trial] = i_walker2.x

    min_x = min(min(final_x_r), min(final_x_i1), min(final_x_i2))
    max_x = max(max(final_x_r), max(final_x_i1), max(final_x_i2))

    bin_x = np.arange(min_x, max_x + 1, 0.5)

    if trial % 100 == 0 and trial > 0:

        print('Trial:', trial)

        plt.figure(tight_layout=True, figsize=(9, 6))

        list_i1 = list(final_x_i1[:trial])
        list_i2 = list(final_x_i2[:trial])
        list_i = list_i1 + list_i2
        list_i = np.array(list_i)

        plt.hist(final_x_r[:trial], bins=bin_x,
                 alpha=0.7, label='Reflective', color='b')
        plt.hist(final_x_i1[:trial], bins=bin_x, alpha=0.7,
                 label='Image 1', histtype='step', linestyle='dashed', color='k')
        plt.hist(final_x_i2[:trial], bins=bin_x, alpha=0.7,
                 label='Image 2', histtype='step', linestyle='dashed', color='k')
        plt.hist(list_i, bins=bin_x, alpha=1.0,
                 label='Total image', histtype='step', color='r')

        plt.xlabel('x')
        plt.ylabel('Count')
        plt.xlim(min_x, max_x)

        plt.axvline(x=xmax, color='k', linestyle='dashed',
                    label='Wall', linewidth=2.0)

        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        plt.savefig('reflective_vs_image.png')

        plt.close()
