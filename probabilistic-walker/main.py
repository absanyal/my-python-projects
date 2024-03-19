import numpy as np
import matplotlib.pyplot as plt
from modules.pwalker import pwalker
from modules.dosplot import dosplot

t_iters = 1000
x0 = 0
p_forward = 0.25
p_backward = 0.25

n_trials = 2000

switch_point1 = 0.3
switch_point2 = 0.6

skip_recording = 500

walker = pwalker(x0, p_forward, p_backward)


t_list = np.arange(t_iters)
x_squared_list = np.zeros(t_iters)

x_list = []

plt.figure(tight_layout=True)

for trial in range(n_trials):
    walker.reset()
    walker.set_p_forward(p_forward)
    walker.set_p_backward(p_backward)
    x0 = walker.get_position0()
    for t in t_list:
        walker.walk()
        x = walker.get_position()
        x_squared_list[t] += (x - x0)**2
        x_list.append(x)
        
        if (t + 1) >= switch_point1 * t_iters:
            walker.set_p_forward(0.5)
            walker.set_p_backward(0.5)
        
        if (t + 1) >= switch_point2 * t_iters:
            walker.set_p_forward(p_forward)
            walker.set_p_backward(p_backward)
    
    x_squared_list_tmp = x_squared_list / (trial + 1)
    
    if trial % skip_recording == 0:
        plt.clf()
        plt.cla()
        plt.plot(t_list, x_squared_list_tmp, 'k', label='Data')
        plt.xlabel(r'$t$')
        plt.ylabel(r'$ \langle x^2 \rangle $')
        plt.title('Trials = {}'.format(trial + 1))
        plt.legend()
        plt.savefig('plots/x_squared_vs_t.pdf')
        
        plt.clf()
        plt.cla()
        
        x_sq_log_list = np.log10(x_squared_list_tmp)
        t_log_list = np.log10(t_list)

        plt.plot(t_log_list, x_sq_log_list, 'k', label='Data')
        plt.xlabel(r'$\log(t)$')
        plt.ylabel(r'$ \log(\langle x^2 \rangle) $')
        plt.title('Trials = {}'.format(trial + 1))
        plt.legend()
        plt.savefig('plots/x_squared_vs_t_log.pdf')
        
        plt.clf()
        plt.cla()
        
        plt.hist(x_list, bins='auto', color='b', label='Data', rwidth=1.0, density=True)
        plt.xlabel(r'$x$')
        plt.ylabel(r'$P(x)$')
        plt.title('Trials = {}'.format(trial + 1))
        plt.legend()
        plt.savefig('plots/x_hist.pdf')

plt.clf()
plt.cla()

x_squared_list = x_squared_list / n_trials

plt.plot(t_list, x_squared_list, 'k', label='Data')
plt.xlabel(r'$t$')
plt.ylabel(r'$ \langle x^2 \rangle $')
plt.title('Trials = {}'.format(n_trials))
plt.legend()
plt.savefig('plots/x_squared_vs_t.pdf')

plt.clf()
plt.cla()

x_sq_log_list = np.log10(x_squared_list)
t_log_list = np.log10(t_list)

plt.plot(t_log_list, x_sq_log_list, 'k', label='Data')
plt.xlabel(r'$\log(t)$')
plt.ylabel(r'$ \log(\langle x^2 \rangle) $')
plt.title('Trials = {}'.format(n_trials))
plt.legend()
plt.savefig('plots/x_squared_vs_t_log.pdf')

plt.clf()
plt.cla()

w_min = min(x_list) - 1
w_max = max(x_list) + 1

num_w = 1000
gamma_val = 5.0

w_list = np.linspace(w_min, w_max, num_w)

x_list = np.array(x_list)

dos = dosplot(w_list, x_list, gamma_val)

plt.plot(w_list, dos, 'b', label='Data', linewidth=0.5)
plt.xlabel(r'$x$')
plt.ylabel(r'$P(x)$')
plt.title('Trials = {}'.format(n_trials))
plt.legend()
plt.savefig('plots/x_hist.pdf')