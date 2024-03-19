import numpy as np
import matplotlib.pyplot as plt
from modules.urn import urn

n_types = 100
n_balls_min = 1
n_balls_max = 2

u = urn(n_types, n_balls_min, n_balls_max)

# print("Initial")
# print(u.balls)

n_iters_total = 100000

t_to_skip = 100

t_list = np.arange(0, n_iters_total, t_to_skip)

n_iters = len(t_list)

numbers_list = np.zeros((n_iters, n_types))
weights_list = np.zeros((n_iters, n_types))


skipping_index = 0
for t_i in range(n_iters_total):
    draw_index, draw_ball = u.draw()
    u.add_ball(draw_index)

    if t_i % t_to_skip == 0:
        # print("Recording: t_i = {} / {}".format(t_i, n_iters_total))
        for n_type_i in range(n_types):
            numbers_list[skipping_index, n_type_i] = u.balls[n_type_i]
            weights_list[skipping_index,
                         n_type_i] = u.probability_list[n_type_i]
        skipping_index += 1


# print("FInal")
# print(u.balls)

# plt.plot(t_list, weights_list)
plt.plot(t_list, numbers_list)
plt.xlabel('Iteration')
# plt.legend(['Type ' + str(i+1) for i in range(n_types)])
plt.ylabel('Number of balls')

# plt.ylim(top = 0.014, bottom = 0.006)

# plt.xscale('log')
# plt.yscale('log')

plt.show()
