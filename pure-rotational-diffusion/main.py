import numpy as np
import matplotlib.pyplot as plt
from modules.brownianengine import brownian_engine
from modules.rod import rod
from numpy import random, sqrt, pi

# Parameters
D = 0.068
dt = 1e-3

n_trials = 2000
n_iters = 30000

initial_angle = np.radians(30)
target_angle = np.radians(90)

print("D = {:.4f}".format(D))
print("dt = {:.4e}".format(dt))
print("n_trials = {}".format(n_trials))
print("n_iters = {}".format(n_iters))
print("Total time = {:.4f}".format(n_iters*dt))

with open("data/info.dat", "w") as f:
    f.write("{:.4f}\n".format(D))
    f.write("{:.4e}\n".format(dt))
    f.write("{}\n".format(n_trials))
    f.write("{}\n".format(n_iters))
    f.write("{:.4f}\n".format(n_iters*dt))
    f.write("{:.2f}\n".format(np.degrees(initial_angle)))
    f.write("{:.2f}\n".format(np.degrees(target_angle)))

print("Initial angle = {:.2f} degree".format( np.degrees(initial_angle) ))
print("Target angle = {:.2f} degree".format( np.degrees(target_angle) ))

print("-"*20)


# Initialize
be = brownian_engine(D, dt)
r = rod(initial_angle)

fp_times = []
fp_times_iter = []

success_counter = 0

# with open("data/timehist.dat", "a") as f:
for trial_i in range(n_trials):
    if trial_i % 100 == 0:
        print("Simulation trial {}".format(trial_i))
    r.reset()
    for iter in range(n_iters):
        be.perturb(r)
        # print("t={:.4f}, angle={:.4f}".format(iter, r.get_angle()))
        if r.get_angle() >= target_angle:
            fp_times.append(iter*dt)
            fp_times_iter.append(iter)
            success_counter += 1
            # print("Final angle: {:.4f}".format(r.get_angle()))
            # f.write("{} {}\n".format(iter, iter*dt))
            break

    with open("data/timehist.dat", "w") as f:
        for i in range(len(fp_times)):
            f.write("{} {:.5f}\n".format(fp_times_iter[i], fp_times[i]))

    # print("Success in {} out of {} trials".format(success_counter, trial_i+1))
    # print("Current success rate: {:.4f}".format(success_counter/(trial_i+1)))
    # print("-"*20)

print("Final success in {} out of {} trials".format(success_counter, n_trials))
print("Success rate: {:.4f}".format(success_counter/n_trials))

# fp_times_cut = []

# cutoff_time = 1


# for time in fptimes:
#     if time <= cutoff_time:
#         fp_times_cut.append(time)

# fp_times_cut = fptimes.copy()

# # bin_interval = 0.01
# # bin_max = 1
# # bins_list = np.arange(0, max(fp_times_cut), bin_interval)

# plt.hist(fp_times_cut, density=True)
# # plt.ylim(top = 1)
# plt.savefig("fptimes.png")
