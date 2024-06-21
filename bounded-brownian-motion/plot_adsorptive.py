import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from modules.dosmaker import make_dos as mdos
from modules.diffusion_solutions import reflective_soln, adsorptive_soln

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 16

plot_histogram = 1
plot_dos = 0

trials, final_x_a = np.loadtxt('adsorptive_walker.txt', unpack=True)

Dx, Dy, Dz, x0, y0, z0, dt, distance_from_wall, num_iters, p_adsorption = np.loadtxt(
    'adsorptive_info.txt', unpack=True)

t_final = num_iters * dt

min_x = min(final_x_a)
max_x = max(final_x_a)

xmax = max(final_x_a)

bin_x = np.arange(min_x, max_x + 1, 1.0)

padding_l = 0
padding_r = 1

gamma = 0.3

w_list = np.linspace(min_x - padding_l, max_x + padding_r, 1000)
x_wall = max(final_x_a)

x_ticks1 = np.arange(0, max_x + 1, 10)
x_ticks2 = np.arange(0, min_x + 1, -10)

x_ticks = np.concatenate((x_ticks2, x_ticks1))

density_a_unfiltered = mdos(w_list, final_x_a, gamma)

density_a = np.zeros_like(density_a_unfiltered)

for wi, w in enumerate(w_list):
    if w < x_wall:
        density_a[wi] = density_a_unfiltered[wi]
    else:
        density_a[wi] = 0

density_a = np.array(density_a)

area_a = np.trapz(density_a, w_list)
density_a /= area_a

# Plot walker density

fig = plt.figure(figsize=(5, 5), tight_layout=True)

if plot_dos:
    plt.plot(w_list, density_a, label='Simulation',
         color='b', linewidth=1, alpha=1.0)

if plot_histogram:
    plt.hist(final_x_a, bins=bin_x, density=True, color='b', alpha=0.5, label='Simulation')

solution_un = adsorptive_soln(w_list - x_wall, distance_from_wall, Dx, t_final)
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
plt.savefig('dos_adsorptive.png')
