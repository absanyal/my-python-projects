import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(0)

dt = 0.01
n = 2000
n_trials = 100
t_list = np.arange(0, n*dt, dt)
D = 1.0
print("{} time points".format(len(t_list)))

corr_list_cumu = np.zeros(n)

plt.figure(tight_layout=True)

for trial in range(n_trials):
    theta_list = np.zeros(n)

    theta_list[0] = 0.0

    # for i in range(1, len(theta_list)):
    # theta_list[i] = theta_list[i-1] + np.random.normal(0, 0.1)
    # t_list[i] = t_list[i-1] + dt

    theta_list = np.random.normal(0, 1, n)
    # theta_list = np.cumsum(np.random.normal(0, 1, n) * np.sqrt(2 * D * dt))

    tau_list = np.zeros_like(t_list)

    for i in range(1, len(t_list)):
        tau_list[i] = t_list[i] - t_list[0]

    corr_list = np.zeros_like(tau_list)

    for tau_i, tau in enumerate(tau_list):
        for i in range(len(theta_list) - tau_i):
            corr_list[tau_i] += theta_list[i] * theta_list[i + tau_i]
        corr_list[tau_i] /= len(theta_list) - tau_i

    corr_list_cumu += corr_list
    corr_list_avg = corr_list_cumu / (trial + 1)

    plt.clf()

    plt.plot(tau_list, corr_list_avg)
    plt.xlabel('Time lag')
    plt.ylabel('Correlation')
    plt.title("Trials: {}".format(trial + 1))
    plt.savefig('corr.png')
