import numpy as np
import matplotlib.pyplot as plt
import rcparams

t_iters = 1000
n_particles = 2
dimension = 1

D_list = [0.1, 1]

dt = 0.1

t_list = np.linspace(0, t_iters*dt, t_iters)

r = np.zeros((t_iters, n_particles, dimension))

for p_i in range(n_particles):
    D = D_list[p_i]
    dr = np.sqrt(2*D*dt)*np.random.randn(t_iters, dimension)
    r[:, p_i, :] = np.cumsum(dr, axis=0)
    r[:, p_i, :] -= r[0, p_i, :]


p_1 = r[:, 0, :]
p_2 = r[:, 1, :]

s = np.linalg.norm(p_1 - p_2, axis=1)

fig, ax = plt.subplots(constrained_layout=True)

if dimension == 1:
    ax.plot(t_list, p_1, c='r')
    ax.plot(t_list, p_2, c='b')
    
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$x$')
elif dimension == 2:
    ax.scatter(p_1[:, 0], p_1[:, 1], c='r', marker='.', s=1, alpha=0.5)
    ax.scatter(p_2[:, 0], p_2[:, 1], c='b', marker='.', s=1, alpha=0.5)

    ax.scatter(p_1[0, 0], p_1[0, 1], c='r', marker='o', s=50)
    ax.scatter(p_2[0, 0], p_2[0, 1], c='b', marker='o', s=50)

    ax.scatter(p_1[-1, 0], p_1[-1, 1], c='r', marker='x', s=50)
    ax.scatter(p_2[-1, 0], p_2[-1, 1], c='b', marker='x', s=50)
    
    ax.set_xlabel(r'$x$')
    ax.set_ylabel(r'$y$')
    
plt.savefig('plots/positions.png')

fig, ax = plt.subplots(constrained_layout=True)

ax.set_xlabel(r'$t$')
ax.set_ylabel(r'$s$')

ax.plot(t_list, s)

plt.savefig('plots/separation.png')