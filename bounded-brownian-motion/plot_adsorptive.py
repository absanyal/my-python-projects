import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from modules.dosmaker import make_dos as mdos

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 16

trials, final_x_a = np.loadtxt('adsorptive_walker.txt', unpack=True)

final_x_i1 = np.loadtxt('adsorptive_i1.txt', unpack=True, usecols=1)
final_x_i2 = np.loadtxt('adsorptive_i2.txt', unpack=True, usecols=1)

min_x = min(min(final_x_a), min(final_x_i1), min(final_x_i2))
max_x = max(max(final_x_a), max(final_x_i1), max(final_x_i2))

xmax = max(final_x_a)

bin_x = np.arange(min_x, max_x + 1, 0.5)

padding = 0
gamma = 0.25

w_list = np.linspace(min_x - padding, max_x + padding, 1000)
x_wall = max(final_x_a)


density_r_unfiltered = mdos(w_list, final_x_a, gamma)

density_r = np.zeros_like(density_r_unfiltered)

for wi, w in enumerate(w_list):
    if w < x_wall:
        density_r[wi] = density_r_unfiltered[wi]
    else:
        density_r[wi] = 0

density_r = np.array(density_r)

area_r = np.trapz(density_r, w_list)
density_r /= area_r

density_i1 = mdos(w_list, final_x_i1, gamma)
density_i2 = mdos(w_list, final_x_i2, gamma)

total_image_unfiltered = (density_i1 - density_i2)

total_image = np.zeros_like(total_image_unfiltered)
for w in w_list:
    for wi, w in enumerate(w_list):
        if w < x_wall:
            total_image[wi] = total_image_unfiltered[wi]
        else:
            total_image[wi] = 0

total_image = np.array(total_image)

total_image_area = np.trapz(total_image, w_list)
total_image /= total_image_area

plt.figure(figsize=(9, 6), constrained_layout=True)

plt.plot(w_list, density_r, label='Adsorptive',
         color='b', linewidth=1, alpha=0.7)

plt.plot(w_list, density_i1, label=r'$I_1$',
         color='k', linewidth=1, alpha=0.5, linestyle='dashed')
plt.plot(w_list, density_i2, label=r'$I_2$',
         color='k', linewidth=1, alpha=0.5, linestyle='dashed')
plt.plot(w_list, total_image, label=r'$I_1 - I_2$',
         color='r', linewidth=1, alpha=0.5)

plt.xlabel(r'$x$')
plt.ylabel(r'$P(x)$')
plt.xlim(min_x - padding, max_x + padding)
plt.ylim(bottom=0)

plt.axvline(x=xmax, color='k', linestyle='dashed',
            label='Wall', linewidth=2.0)

plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')

plt.savefig('adsorptive_dos.png')

plt.close()
