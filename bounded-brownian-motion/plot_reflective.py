import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

from modules.dosmaker import make_dos as mdos

mpl.rcParams['axes.labelsize'] = 20
mpl.rcParams['xtick.labelsize'] = 20
mpl.rcParams['ytick.labelsize'] = 20
mpl.rcParams['legend.fontsize'] = 16

trials, final_x_r, final_x_i1, final_x_i2 = np.loadtxt(
    'reflective_walker.txt', unpack=True)

min_x = min(min(final_x_r), min(final_x_i1), min(final_x_i2))
max_x = max(max(final_x_r), max(final_x_i1), max(final_x_i2))

xmax = max(final_x_r)

bin_x = np.arange(min_x, max_x + 1, 0.5)

# list_i1 = list(final_x_i1)
# list_i2 = list(final_x_i2)
# list_i = list_i1 + list_i2
# list_i = np.array(list_i)

# plt.figure(constrained_layout =True, figsize=(9, 6))

# plt.hist(final_x_r, bins=bin_x,
#          alpha=0.7, label='Reflective', color='b')
# plt.hist(final_x_i1, bins=bin_x, alpha=0.7,
#          label='Image 1', histtype='step', linestyle='dashed', color='k')
# plt.hist(final_x_i2, bins=bin_x, alpha=0.7,
#          label='Image 2', histtype='step', linestyle='dashed', color='k')
# plt.hist(list_i, bins=bin_x, alpha=1.0,
#          label='Total image', histtype='step', color='r')

# plt.xlabel('x')
# plt.ylabel('Count')
# plt.xlim(min_x, max_x)

# plt.axvline(x=xmax, color='k', linestyle='dashed',
#             label='Wall', linewidth=2.0)

# plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# plt.savefig('reflective_hist.png')

# plt.close()

padding = 0
gamma = 0.25

w_list = np.linspace(min_x - padding, max_x + padding, 1000)
x_wall = max(final_x_r)


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



density_i1 = mdos(w_list, final_x_i1, gamma)
density_i2 = mdos(w_list, final_x_i2, gamma)

total_image = density_i1 + density_i2

plt.figure(figsize=(9, 6), constrained_layout=True)

plt.plot(w_list, density_r, label='Reflective',
         color='b', linewidth=1, alpha=0.7)

plt.plot(w_list, density_i1, label=r'$I_1$',
         color='k', linewidth=1, alpha=0.5, linestyle='dashed')
plt.plot(w_list, density_i2, label=r'$I_2$',
         color='k', linewidth=1, alpha=0.5, linestyle='dashed')
plt.plot(w_list, total_image, label=r'$I_1 + I_2$',
         color='r', linewidth=1, alpha=0.5)

plt.xlabel(r'$x$')
plt.ylabel(r'$P(x)$')
plt.xlim(min_x - padding, max_x + padding)
plt.ylim(bottom=0)

plt.axvline(x=xmax, color='k', linestyle='dashed',
            label='Wall', linewidth=2.0)

plt.legend(bbox_to_anchor=(1.0, 1), loc='upper left')

plt.savefig('reflective_dos.png')

plt.close()
