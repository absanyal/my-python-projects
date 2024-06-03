import numpy as np
from modules.lattice import lattice
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation

Lx, Ly = 100, 100

lat = lattice(Lx, Ly)

occupancy = 0.05

particles = int(Lx*Ly * occupancy)
if particles == 0:
    particles = 1
if particles >= Lx*Ly:
    particles = Lx*Ly - 1

t_iters = 1000

sites_to_fill = np.random.choice(Lx*Ly, particles, replace=False)

for site in sites_to_fill:
    i, j = lat.index_to_coordinates(site)
    lat.sites[i, j] = 1

fig, ax = plt.subplots()
ims = []

for i in range(t_iters):
    ims.append([plt.imshow(lat.sites, cmap='viridis')])
    lat.update()

ani = ArtistAnimation(fig, ims, interval=1/60, blit=True)

plt.show()