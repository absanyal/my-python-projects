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

wall_size = prm.bound_size

bounds = wall(-wall_size, wall_size, -wall_size,
              wall_size, -wall_size, wall_size)
w = walker(0, 0, 0, D, dt, bounds)

with open('data/pos.txt', 'w') as pos_f:
    pos_f.write('#t\tx\ty\tz\n')
    for i in range(iterations):
        t = i*dt
        x, y, z = w.get_pos()

        pos_f.write('{}\t{}\t{}\t{}\n'.format(t, x, y, z))

        w.walk()
