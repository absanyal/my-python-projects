import numpy as np
from modules.distributions import firstpassage

info = np.loadtxt("data/info.dat", unpack=True)
D = info[0]
dt = info[1]
n_trials = info[2]
n_iters = info[3]
total_time = info[4]
initial_angle = info[5]
target_angle = info[6]

Dinput = D
theta0 = np.radians(initial_angle)
max_t = total_time

t = np.linspace(0.0001, max_t, 1000)

with open("data/firstpassage.dat", "w") as f:
    for tt in t:
        f.write("{:.4f} {:.4f}\n".format(tt, Dinput * firstpassage(Dinput * tt, theta0)))

# fpd = np.zeros(len(t))
# for i in range(len(t)):
#     fpd[i] = firstpassage(t[i], theta0)

# N = np.trapz(fpd, t)
# fpd = fpd / N

# with open("data/firstpassage.dat", "w") as f:
#     for i, tt in enumerate(t):
#         f.write("{:.4f} {:.4f}\n".format(tt, fpd[i]))