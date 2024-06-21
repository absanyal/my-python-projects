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
num_trials = 50000
num_iters = 3000

# Define the wall
xmin = -30
xmax = 10

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

final_x_r = np.zeros(num_trials)

with open('reflective_info.txt', 'w') as file:
    file.write(
        "#Dx \t Dy \t Dz \t x0 \t y0 \t z0 \t dt \t distance_from_wall \t n_iters\n")
    file.write("{} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {}\n".format(
        Dx, Dy, Dz, x0, y0, z0, dt, distance_from_wall, num_iters))

with open('reflective_walker.txt', 'w') as file:
    file.write('#Trial\tReflective\n')

with open('reflective_walker.txt', 'a') as file:
    for trial in range(num_trials):

        r_walker.reset()

        for ti in range(num_iters):

            r_walker.step()

        final_x_r[trial] = r_walker.x
        
        file.write('{}\t{}\n'.format(trial, final_x_r[trial]))

        min_x = min(final_x_r)
        max_x = max(final_x_r)

        bin_x = np.arange(min_x, max_x + 1, 0.5)

        if trial % 1000 == 0 and trial > 0:

            print('Trial:', trial)
