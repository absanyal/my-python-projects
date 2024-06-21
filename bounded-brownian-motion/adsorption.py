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

p_adsorption = 1.0

this_wall = wall(xmin, xmax, ymin, ymax, zmin, zmax, adsorption_p=p_adsorption)

# Define the adsorptive walker
distance_from_wall = 10.0

Dx = 1.0
Dy = 0.0
Dz = 0.0
D = np.array([Dx, Dy, Dz])

x0 = xmax - distance_from_wall
y0 = 0
z0 = 0

dt = 0.02

a_walker = walker(D, x0, y0, z0, dt, this_wall)

final_x_a = []

num_adsorped = 0

with open('adsorptive_info.txt', 'w') as file:
    file.write(
        "#Dx \t Dy \t Dz \t x0 \t y0 \t z0 \t dt \t distance_from_wall \t n_iters \t p_adsorption\n")
    file.write("{} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {} \t {}\n".format(
        Dx, Dy, Dz, x0, y0, z0, dt, distance_from_wall, num_iters, p_adsorption))

with open('adsorptive_walker.txt', 'w') as file:
    file.write('#Trial\tAdsorptive\n')

adsorption_happened = False

with open('adsorptive_walker.txt', 'a') as f_w:
    for trial in range(num_trials):

        a_walker.reset()
        adsorption_happened = False

        for ti in range(num_iters):
            a_walker.step()

        if a_walker.isadsorped == False:
            final_x_a.append(a_walker.x)
        else:
            num_adsorped += 1
            adsorption_happened = True

        min_x = min(final_x_a)
        max_x = max(final_x_a)

        bin_x = np.arange(min_x, max_x + 1, 1.0)

        if adsorption_happened == False:
            f_w.write('{}\t{}\n'.format(trial, final_x_a[-1]))

        if trial % 100 == 0 and trial > 0:

            print('Trial:', trial)
            print('Adsorped: {} / {}'.format(num_adsorped, trial))
