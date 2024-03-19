import numpy as np
import matplotlib.pyplot as plt

from modules.walker import walker
from modules.wall import wall
import modules.parameters as prm

Dx = prm.Dx
Dy = prm.Dy
Dz = prm.Dz
D = np.array([Dx, Dy, Dz])

dt = prm.dt

iterations = prm.iterations

trials = prm.trials

record_skip = 20

# alpha_val = max(1/trials, 0.005)
alpha_val = 0.002

wall_size = prm.bound_size

bounds = wall(-wall_size, wall_size, -wall_size, wall_size, -wall_size, wall_size)
w = walker(-190, 0, 0, D, dt, bounds)

t = np.arange(0, iterations*dt, dt)

fig, ax = plt.subplots(1, 3, figsize=(15, 5), tight_layout=True)
axis_buffer = 1.5

for trial in range(trials):
    if (trial+1) % record_skip == 0:
        print('Simulating trial', trial+1, 'of', trials, '...')

    x = np.zeros(iterations)
    y = np.zeros(iterations)
    z = np.zeros(iterations)
    
    w.reset()


    for i in range(iterations):
        x[i], y[i], z[i] = w.get_pos()
        w.walk()


    ax[0].scatter(x, y, s=0.2, alpha=alpha_val, c='k')
    ax[0].set_xlabel('x', fontsize=18)
    ax[0].set_ylabel('y', fontsize=18)
    ax[0].set_title('x-y plane', fontsize=18)
    ax[0].set_xlim(-wall_size - axis_buffer, wall_size + axis_buffer)
    ax[0].set_ylim(-wall_size - axis_buffer, wall_size + axis_buffer)

    ax[1].scatter(x, z, s=0.2, alpha=alpha_val, c='k')
    ax[1].set_xlabel('x', fontsize=18)
    ax[1].set_ylabel('z', fontsize=18)
    ax[1].set_title('x-z plane', fontsize=18)
    ax[1].set_xlim(-wall_size - axis_buffer, wall_size + axis_buffer)
    ax[1].set_ylim(-wall_size - axis_buffer, wall_size + axis_buffer)

    ax[2].scatter(y, z, s=0.2, alpha=alpha_val, c='k')
    ax[2].set_xlabel('y', fontsize=18)
    ax[2].set_ylabel('z', fontsize=18)
    ax[2].set_title('y-z plane', fontsize=18)
    ax[2].set_xlim(-wall_size - axis_buffer, wall_size + axis_buffer)
    ax[2].set_ylim(-wall_size - axis_buffer, wall_size + axis_buffer)

    if (trial+1) % record_skip == 0:
        plt.savefig('plots/3d_slices.png')