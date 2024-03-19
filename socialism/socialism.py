import numpy as np
import matplotlib.pyplot as plt

pop = 10000

t_steps = 100000

percentage = 0.1

# money_list = np.random.beta(2, 2, pop)
money_list = np.random.uniform(0.9, 1.0, pop)

plt.hist(money_list, bins=50)
plt.show()

for t in range(t_steps):
    p1, p2 = np.random.choice(range(pop), 2)
    m1 = money_list[p1]
    m2 = money_list[p2]

    # print("t = ", t)
    # print("Person", p1,  "has ", m1)
    # print("Person", p2,  "has ", m2)

    if m1 > m2:
        e = percentage * m1

        m1 -= e
        m2 += e
        # print("Giving", e,  "to person", p2)
    elif m1 < m2:
        e = percentage * m2
        m1 += e
        m2 -= e
        # print("Giving", e, "to person", p1)

    money_list[p1] = m1
    money_list[p2] = m2

    # print("Person", p1,  "has ", m1)
    # print("Person", p2,  "has ", m2)
    # print("-------Exchange complete---------")

    if t % 1000 == 0:
        print("t = ", t)

plt.hist(money_list, bins=50)
plt.show()
