import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from modules.diffusion_solutions import reflective_soln, adsorptive_soln

from modules.dosmaker import make_dos as mdos

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 16

plot_histogram = 1
plot_dos = 0

trials, final_x_r = np.loadtxt(
    'reflective_walker.txt', unpack=True)

min_x = min(final_x_r)
max_x = max(final_x_r)

xmax = max(final_x_r)

bin_x = np.arange(min_x, max_x + 1, 1.0)

Dx, Dy, Dz, x0, y0, z0, dt, distance_from_wall, num_iters = np.loadtxt(
    'reflective_info.txt', unpack=True)

t_final = num_iters * dt


padding_l = 0
padding_r = 1

gamma = 0.3

w_list = np.linspace(min_x - padding_l, max_x + padding_r, 1000)
x_wall = max(final_x_r)

x_ticks1 = np.arange(0, max_x + 1, 10)
x_ticks2 = np.arange(0, min_x + 1, -10)

x_ticks = np.concatenate((x_ticks2, x_ticks1))


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

fig = plt.figure(figsize=(5, 5), tight_layout=True)

if plot_dos:
    plt.plot(w_list, density_r, label='Simulation',
             color='b', linewidth=1, alpha=1.0)

if plot_histogram:
    plt.hist(final_x_r, bins=bin_x, density=True, color='b',
             label='Simulation', rwidth=1.0, edgecolor='b', alpha = 0.5)

# Analytic solution

solution_un = reflective_soln(w_list - x_wall, distance_from_wall, Dx, t_final)
solution = np.zeros_like(solution_un)
for wi, w in enumerate(w_list):
    if w < x_wall:
        solution[wi] = solution_un[wi]
    else:
        solution[wi] = 0

solution_nf = np.trapz(solution, w_list)
solution /= solution_nf

plt.plot(w_list, solution, label='Theory',
         color='r', linewidth=1, alpha=1.0)

plt.xlabel(r'$x$')
plt.ylabel(r'$P(x)$')

plt.xlim(min_x - padding_l, max_x + padding_r)
plt.ylim(bottom=0)

plt.xticks(x_ticks)

plt.axvline(x=xmax, color='k', linestyle='dashed',
            label='Wall', linewidth=1.0, alpha=0.5)

# ax.legend(bbox_to_anchor=(1.0, 1), loc='upper left')
plt.legend(loc='upper left', fancybox=True, framealpha=0.0)
plt.savefig('dos_reflective.pdf')
