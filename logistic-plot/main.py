import numpy as np
import matplotlib.pyplot as plt


def final_values(x0, r, alpha=1.0):
    final_values = []
    
    for i in range(500):
        x0 = (r) * x0 * ((1 - x0) ** alpha)
        if i >= 400:
            final_values.append(x0)
    
    final_values = np.array(final_values)
    final_values = np.unique(final_values)
    return final_values

x0 = 0.9
r_range = np.linspace(0, 4, 5000)
alpha = 1

x_list = []
r_list = []

for r_i in r_range:
    x = final_values(x0, r_i, alpha)
    x_list.extend(x)
    r_list.extend([r_i] * len(x))

plt.scatter(r_list, x_list, s=0.1, c='black', alpha=0.5)
plt.xlabel('r')
plt.ylabel('x')
plt.show()