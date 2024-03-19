import numpy as np
import matplotlib.pyplot as plt
import modules.brownian as brn

Dx, Dy, Dz = [1, 0, 1]

p1 = brn.particle(0, 0, 0)

dt = 0.001

t_iters = 5000

t_list = np.zeros(t_iters)
for i in range(t_iters):
    t_list[i] = i * dt

n_trials = 5000

dist_sq = np.zeros(t_iters)

for n in range(n_trials):
    if (n+1) % 100 == 0:
        print('Trial {}/{}'.format(n+1, n_trials))
    p1.reset()
    pos_0 = p1.get_position()
    for t_i in range(len(t_list)):
        p1.brownian_move(Dx, Dy, Dz, dt)
        pos_t = p1.get_position()
        disp = pos_t - pos_0
        dist_sq[t_i] += np.dot(disp, disp)
        
dist_sq /= n_trials

with open('data/distance.dat', 'w') as f:
    for i in range(t_iters):
        f.write('{}\t{}\n'.format(
            t_list[i], dist_sq[i]))
