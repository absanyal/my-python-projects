import numpy as np

def costfunction(f_target, f_train, domain):
    target_vals = f_target.value(domain)
    train_vals = f_train.value(domain)
    cost = 0
    for i in range(len(domain)):
        cost += ((target_vals[i] - train_vals[i]) / target_vals[i])**2
    cost = np.sqrt(cost)
    cost /= len(domain)
    cost = np.log10(cost)
    return cost