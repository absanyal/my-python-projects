import numpy as np
import matplotlib.pyplot as plt
import rcparams
from scipy.optimize import curve_fit

import matplotlib

def linear(x, a):
    return a*x

t_list, avg_d_theta_sq_list = np.loadtxt('d_theta_sq_vs_t.txt', unpack=True)

p_opt, p_cov = curve_fit(linear, t_list, avg_d_theta_sq_list)
D_rot_measured = p_opt[0]/2

y_fit = linear(t_list, *p_opt)

plt.figure(figsize=(5, 5))

plt.plot(t_list, avg_d_theta_sq_list, label='Simulation', color='black')
plt.plot(t_list, y_fit, label=r'Fit: $D_{{\mathrm{{rot}}}} = {:.4f}$'.format(D_rot_measured), color='red', ls='--')

plt.legend()

plt.xlabel(r'$t/\tau$')
plt.ylabel(r'$\langle \Delta \theta^2 \rangle$')

plt.xlim(min(t_list), max(t_list))
plt.ylim(min(avg_d_theta_sq_list), max(avg_d_theta_sq_list))

plt.savefig('plots/d_theta_sq_vs_t.pdf')
plt.clf()
plt.cla()
#

t_list, avg_d_s_s_q_list = np.loadtxt('d_s_sq_vs_t.txt', unpack=True)

p_opt, p_cov = curve_fit(linear, t_list, avg_d_s_s_q_list)
D_tr_measured = p_opt[0]/6

y_fit = linear(t_list, *p_opt)

plt.plot(t_list, avg_d_s_s_q_list, label='Simulation', color='black')
plt.plot(t_list, y_fit, label=r'Fit: $D = {:.4f}$'.format(D_tr_measured), color='red', ls='--')

plt.legend()

plt.xlim(min(t_list), max(t_list))
plt.ylim(min(avg_d_s_s_q_list), max(avg_d_s_s_q_list))

plt.xlabel(r'$t/\tau$')
plt.ylabel(r'$\langle \Delta s^2_{{\mathrm{{CoM}}}} \rangle$')

plt.savefig('plots/d_s_sq_vs_t.pdf')