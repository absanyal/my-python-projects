import numpy as np
import matplotlib.pyplot as plt
from modules.geneticf import geneticf
from modules.costfunction import costfunction

target_params = np.random.uniform(-5, 5, 4)
# target_params = [1, 2, 30, -1]

f_target = geneticf(target_params)

x = np.linspace(-5, 5, 1000)

f_train = geneticf(np.zeros(len(target_params)))
# f_train = geneticf(np.random.uniform(-10, 10, len(target_params)))

t_iters = 100000

fig, ax = plt.subplots(1, 2, tight_layout=True, figsize=(10, 5))

cost_list = []
cost_time = []
cost_diff_list = []

old_cost = costfunction(f_target, f_train, x)
new_cost = 1

old_avg_cost_diff = 1000

for t_i in range(t_iters):
    train_params = f_train.get_params()
    old_params = train_params.copy()

    old_cost = costfunction(f_target, f_train, x)

    for i in range(len(train_params)):
        train_params[i] += np.random.normal(0, 0.01)

    f_train.set_params(train_params)

    new_cost = costfunction(f_target, f_train, x)

    # cost_list.append(new_cost)

    if new_cost < old_cost:
        # cost_list.append(new_cost)
        # cost_time.append(t_i+1)
        r = np.random.uniform()
        if r > 0.7:
            f_train.set_params(train_params)
    else:
        f_train.set_params(old_params)

    if (t_i+1) % 100 == 0:
        print("{}: C={:.3f}".format(t_i+1, new_cost))
        print("Target \t Trained")
        print("------ \t -------")
        for i in range(len(target_params)):
            print("{:.3f} \t {:.3f}".format(
                target_params[i], f_train.get_params()[i]))
        print("-"*20)
    if (t_i+1) % 100 == 0:
        # cost_list.append(new_cost)
        cost_list.append(new_cost)
        cost_time.append(t_i+1)

        ax[0].cla()
        # ax[0].plot(cost_time, cost_list, color='blue', label='Cost')
        ax[0].scatter(cost_time, cost_list, color='blue',
                      label='Cost', s=5, alpha=0.3)

        ax[0].set_xlabel('Time')
        ax[0].set_ylabel('Cost')

    if (t_i+1) % 1000 == 0:
        ax[1].cla()

        ax[1].plot(x, f_target.value(x), label='Target function',
                   color='black', linestyle='--', alpha=0.5, linewidth=3)
        ax[1].plot(x, f_train.value(x), label='Trained function',
                   color='red', alpha=0.5)

        ax[1].set_xlabel(r'$x$')
        ax[1].set_ylabel(r'$f(x)$')

        plt.legend(['Target function', 'Trained function'])

        plt.savefig('mcparams.pdf')

    # cost_diff = np.abs((new_cost - old_cost) / old_cost)
    # cost_diff_list.append(cost_diff)

    # avg_cost_diff = np.mean(cost_diff_list[-10:])

    # if (abs((avg_cost_diff - old_avg_cost_diff) / old_avg_cost_diff)) < 1e-6:
    #     break
    
    # old_avg_cost_diff = avg_cost_diff

ax[0].cla()
ax[1].cla()

ax[0].plot(cost_time, cost_list, label='Cost', color='blue')

ax[1].plot(x, f_target.value(x), label='Target function',
           color='black', linestyle='--', alpha=0.5, linewidth=3)
ax[1].plot(x, f_train.value(x), label='Trained function',
           color='red', alpha=1.0)

plt.legend(['Target function', 'Trained function'])

plt.savefig('mcparams.pdf')

# plt.figure(tight_layout=True)
# plt.plot(cost_time, cost_list, label='Cost', color='blue')
# # plt.scatter(cost_time, cost_list, label='Cost', color='blue')
# # plt.xscale('log')
# # plt.yscale('log')
# plt.savefig('cost.pdf')

print("Final parameters")
print("Target \t Trained")
print("------ \t -------")
for i in range(len(target_params)):
    print("{:.3f} \t {:.3f}".format(target_params[i], f_train.get_params()[i]))

# plt.figure(tight_layout=True)
# plt.plot(x, f_target.value(x), label='Target function', color='black', linestyle='--', alpha=0.5, linewidth=3)
# plt.plot(x, f_train.value(x), label='Trained function', color='red')

# plt.legend()

# plt.savefig('functions.pdf')
