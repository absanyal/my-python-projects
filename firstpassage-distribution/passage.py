import numpy as np
from modules.distributions import firstpassage, wald


t_list = np.linspace(0.001, 5, 3000)

theta_list = [0, 30, 45, 60]

with open('data/theta_list.txt', 'w') as f:
    for theta in theta_list:
        f.write('{}\n'.format(theta))

for theta_i in range(len(theta_list)):
    theta = np.radians(theta_list[theta_i])
    print('Generating data: {}/{} theta = {} degree'.format(theta_i+1,
          len(theta_list), theta_list[theta_i]))
    with open('data/firstpassage_{}.txt'.format(theta_i), 'w') as f, open('data/wald_{}.txt'.format(theta_i), 'w') as w:
        for ti in (range(len(t_list))):
            f_val = firstpassage(t_list[ti], theta)
            w_val = wald(t_list[ti], theta)
            f.write('{}\t{}\n'.format(t_list[ti], f_val))
            w.write('{}\t{}\n'.format(t_list[ti], w_val))
