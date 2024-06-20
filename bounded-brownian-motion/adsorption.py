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
num_iters = 1000

# Define the wall
xmin = -30
xmax = 30

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

# Define the image walker 1
Dx = 1.0
Dy = 0.0
Dz = 0.0

D = np.array([Dx, Dy, Dz])

x0 = xmax - distance_from_wall
y0 = 0
z0 = 0

dt = 0.02

image_walker1 = walker(D, x0, y0, z0, dt, None)

# Define the image walker 2
Dx = 1.0
Dy = 0.0
Dz = 0.0

D = np.array([Dx, Dy, Dz])

x0 = xmax + distance_from_wall
y0 = 0
z0 = 0

dt = 0.02

image_walker2 = walker(D, x0, y0, z0, dt, None)

final_x_a = []
final_x_i1 = []
final_x_i2 = []

num_adsorped = 0

with open('adsorptive_walker.txt', 'w') as file:
    file.write('#Trial\tAdsorptive\n')

with open('adsorptive_i1.txt', 'w') as file:
    file.write('#Trial\tImage 1\n')

with open('adsorptive_i2.txt', 'w') as file:
    file.write('#Trial\tImage 2\n')

adsorption_happened = False
    
with open('adsorptive_walker.txt', 'a') as f_w, open('adsorptive_i1.txt', 'a') as f_i1, open('adsorptive_i2.txt', 'a') as f_i2:
    for trial in range(num_trials):

        a_walker.reset()
        image_walker1.reset()
        image_walker2.reset()
        adsorption_happened = False

        for ti in range(num_iters):
            a_walker.step()
            image_walker1.step()
            image_walker2.step()

        if a_walker.isadsorped == False:
            final_x_a.append(a_walker.x)
        else:
            num_adsorped += 1
            adsorption_happened = True

        final_x_i1.append(image_walker1.x)
        final_x_i2.append(image_walker2.x)

        min_x = min(min(final_x_a), min(final_x_i1), min(final_x_i2))
        max_x = max(max(final_x_a), max(final_x_i1), max(final_x_i2))

        bin_x = np.arange(min_x, max_x + 1, 1.0)
        
        if adsorption_happened == False:
            f_w.write('{}\t{}\n'.format(trial, final_x_a[-1]))
        
        f_i1.write('{}\t{}\n'.format(trial, final_x_i1[-1]))
        f_i2.write('{}\t{}\n'.format(trial, final_x_i2[-1]))

        if trial % 100 == 0 and trial > 0:

            print('Trial:', trial)
            print('Adsorped: {} / {}'.format(num_adsorped, trial))

            # plt.figure(tight_layout=True, figsize=(9, 6))

            # plt.xlabel('x')
            # plt.ylabel('Count')
            # plt.xlim(min_x, max_x)

            # plt.hist(final_x_a, bins=bin_x, color='blue', edgecolor=None,
            #         alpha=0.7, rwidth=1.0, density=False, label='Adsorptive')
            # plt.hist(final_x_i1, bins=bin_x, color='black',
            #         alpha=0.7, rwidth=1.0, density=False, linestyle='dashed', histtype='step', label='Image 1')
            # plt.hist(final_x_i2, bins=bin_x, color='black',
            #         alpha=0.7, rwidth=1.0, density=False, linestyle='dashed', histtype='step', label='Image 2')

            # plt.axvline(x=xmax, color='k', linestyle='dashed',
            #             label='Wall', linewidth=2.0)

            # plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

            # plt.savefig('adsorptive_wall.png')

            # plt.close()
