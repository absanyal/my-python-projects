import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

from modules.walker import walker
from modules.wall import wall
import modules.parameters as prm

def f(x, m, c):
    return m*x + c

Dx = prm.Dx
Dy = prm.Dy
Dz = prm.Dz
D = np.array([Dx, Dy, Dz])

dimension = prm.dimension

dt = prm.dt

iterations = prm.iterations

trials = prm.trials

bound_size = prm.bound_size

bounds = wall(-bound_size, bound_size, -bound_size, bound_size, -bound_size, bound_size)
w = walker(0, 0, 0, D, dt, bounds)

x = np.zeros((trials, iterations))
y = np.zeros((trials, iterations))
z = np.zeros((trials, iterations))

ds2_avg = np.zeros(iterations)

t = np.arange(0, iterations*dt, dt)

plt.figure(tight_layout=True)

for trial in range(trials):
    if (trial+1) % 50 == 0:
        print('Simulating trial', trial+1, 'of', trials, '...')
    
    w.reset()

    for i in range(iterations):
        x[trial, i], y[trial, i], z[trial, i] = w.get_pos()
        w.walk()
    
    dx = x[trial, :] - x[trial, 0]
    dy = y[trial, :] - y[trial, 0]
    dz = z[trial, :] - z[trial, 0]
    
    ds2 = dx**2 + dy**2 + dz**2
    
    ds2_avg += ds2
    
    ds2_current_avg = ds2_avg/(trial+1)
    
    if (trial+1) % 50 == 0:
        plt.clf()
        plt.cla()
        plt.plot(t, ds2_current_avg, lw=2, c='k', label='Simulation')
        plt.xlabel(r'$t/\tau$', fontsize=18)
        plt.ylabel(r'$\langle r^2 \rangle$', fontsize=18)
        
        fit_params, fit_cov = curve_fit(f, t, ds2_current_avg)
        fitline = f(t, *fit_params)
        plt.plot(t, fitline, lw=2, c='r', label='Fit')
        plt.legend(fontsize=14)
        
        plt.title('Trials: {}   D: {:.4f}'.format(trial+1, fit_params[0]/(2*dimension)), fontsize=18)
        
        plt.savefig('plots/ensemble.pdf')

ds2_avg /= trials

fit_params, fit_cov = curve_fit(f, t, ds2_avg)

Diffusion_coefficient = fit_params[0]/(2*dimension)

print('Diffusion coefficient: {:.4f}'.format(Diffusion_coefficient))

fitline = f(t, *fit_params)

# plt.figure(tight_layout=True)

plt.clf()
plt.cla()

plt.plot(t, ds2_avg, lw=2, c='k', label='Simulation')
plt.xlabel(r'$t/\tau$', fontsize=18)
plt.ylabel(r'$\langle r^2 \rangle$', fontsize=18)
plt.title('Trials: {}   D: {:.4f}'.format(trials, Diffusion_coefficient), fontsize=18)

plt.plot(t, fitline, lw=2, c='r', label='Fit')

plt.legend(fontsize=18)

plt.savefig('plots/ensemble.pdf')

with open('data/result_ensemble.txt', 'w') as ens_f:
    ens_f.write('t\tds2_avg\n')
    for i in range(iterations):
        ens_f.write('{}\t{}\n'.format(t[i], ds2_avg[i]))
    
    