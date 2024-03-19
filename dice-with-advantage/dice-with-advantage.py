import numpy as np
import matplotlib.pyplot as plt

# m-sided die
m = 20

# Roll n dice
n = 2

# Conduct t trials
t_max = 3000000


def roll_nDm(n, m):
    return np.random.randint(low=1, high=m+1, size=n)


def advantage(dice):
    return max(dice)


def disadvantage(dice):
    return min(dice)


outcomes = []

for t in range(t_max):
    roll = advantage(roll_nDm(n, m))
    outcomes.append(roll)

print("Average value =", np.mean(outcomes))
print("Theoretical average value =", 2 * m / 3)
print("Theoretical scaled average value =", 2 / 3)
print("Scaled average value =", np.mean(outcomes) / m)

# plt.hist(outcomes, density=True, bins = m)
# plt.show()
