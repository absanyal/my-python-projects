import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from modules.diffusion_solutions import reflective_soln, adsorptive_soln

from modules.dosmaker import make_dos as mdos

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 16

plot_histogram = 0

trials, final_x_r = np.loadtxt(
    'reflective_walker.txt', unpack=True)

min_x = min(final_x_r)
max_x = max(final_x_r)

xmax = max(final_x_r)

bin_x = np.arange(min_x, max_x + 1, 0.5)

Dx, Dy, Dz, x0, y0, z0, dt, distance_from_wall, num_iters = np.loadtxt(
    'reflective_info.txt', unpack=True)

D = Dx
t_final = num_iters * dt


padding = 0
gamma = 0.3

w_list = np.linspace(min_x - padding, max_x + padding, 1000)
x_wall = max(final_x_r)

# Plot walker density

density_r_unfiltered = mdos(w_list, final_x_r, gamma)
density_r = np.zeros_like(density_r_unfiltered)

for wi, w in enumerate(w_list):
    if w < x_wall:
        density_r[wi] = density_r_unfiltered[wi]
    else:
        density_r[wi] = 0

density_r = np.array(density_r)

area_r = np.trapz(density_r, w_list)
density_r /= area_r

fig = plt.figure(figsize=(8.2, 6), constrained_layout=True)
ax = fig.add_subplot(111, box_aspect=1)

ax.plot(w_list, density_r, label='Particle',
        color='b', linewidth=1, alpha=1.0)

if plot_histogram:
    ax.hist(final_x_r, bins=bin_x, density=True, color='b', alpha=0.5)

# Analytic solution

solution_un = reflective_soln(w_list - x_wall, distance_from_wall, D, t_final)
solution = np.zeros_like(solution_un)
for wi, w in enumerate(w_list):
    if w < x_wall:
        solution[wi] = solution_un[wi]
    else:
        solution[wi] = 0

solution_nf = np.trapz(solution, w_list)
solution /= solution_nf

ax.plot(w_list, solution, label='Exact',
         color='r', linewidth=1, alpha=1.0)

ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$P(x)$')
ax.set_xlim(min_x - padding, max_x + padding)
ax.set_ylim(bottom=0)

ax.axvline(x=xmax, color='k', linestyle='dashed',
           label='Wall', linewidth=2.0)
ax.legend(bbox_to_anchor=(1.0, 1), loc='upper left')
plt.savefig('reflective_dos.png')
