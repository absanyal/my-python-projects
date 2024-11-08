import numpy as np
import matplotlib.pyplot as plt
import rcparams

n_trials = 100000
t_iters = 1000

dt = 0.1

n_particles = 2
dimension = 4

D_list = [1, 1]

t_list = np.linspace(0, t_iters*dt, t_iters)
s_list = np.zeros(n_trials)

for trial_i in range(n_trials):

    r = np.zeros((t_iters, n_particles, dimension))

    for p_i in range(n_particles):
        D = D_list[p_i]
        dr = np.sqrt(2*D*dt)*np.random.randn(t_iters, dimension)
        r[:, p_i, :] = np.cumsum(dr, axis=0)
        r[:, p_i, :] -= r[0, p_i, :]


    p_1 = r[:, 0, :]
    p_2 = r[:, 1, :]

    s = np.linalg.norm(p_1 - p_2, axis=1)

    s_list[trial_i] = s[-1]
    
    percent = (trial_i+1)/n_trials*100
    if (trial_i+1) % 10000 == 0:
        print('{} / {} | {:.2f}%'.format(trial_i+1, n_trials, percent))

avg_s = np.mean(s_list)

fig, ax = plt.subplots(constrained_layout=True)

ax.hist(s_list, bins='auto', density=True, color='blue')

ax.set_xlabel('Final separation distance')
ax.set_ylabel('Probability density')

ax.axvline(avg_s, color='red', linestyle='--', label=r'$\langle s \rangle = {:.2f}$'.format(avg_s))

ax.legend()

plt.savefig('plots/separation_dist.png')