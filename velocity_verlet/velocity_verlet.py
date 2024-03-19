import numpy as np
import matplotlib.pyplot as plt

m = 1
k = 1

wf = 1
kf = 0.0
Fext0 = 1.0

gamma = 0.01

dt = 0.01

t_stop = 5000

v0 = 0.0
x0 = 1.0

v_list = [v0]
x_list = [x0]
t_list = [0]

t = 0
v = v0
x = x0


def Fext(x, t):
    return Fext0 * np.cos(wf * t + kf * x)


while (t < t_stop):
    a = (1/m) * (-k * x - gamma * v + Fext(x, t))
    x_new = x + v * dt + 0.5 * a * pow(dt, 2)
    a_new = (1/m) * (-k * x_new - gamma * v + Fext(x_new, t))
    v_new = v + 0.5 * (a + a_new) * dt

    x = x_new
    v = v_new
    t += dt

    x_list.append(x)
    v_list.append(v)
    t_list.append(t)

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)  # row 1, col 2 index 1
plt.plot(t_list, x_list, label="x")
# plt.plot(t_list, v_list, label="v")
plt.xlabel("t")
plt.legend(loc="best")

plt.subplot(1, 2, 2)  # index 2
plt.plot(x_list, v_list)
plt.xlabel("x")
plt.ylabel("v")
# plt.xlim(-1.2, 1.2)
# plt.ylim(-1.2, 1.2)

plt.show()

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)  # row 1, col 2 index 1
plt.hist(x_list, bins=100)
plt.xlabel("x")

plt.subplot(1, 2, 2)  # index 2
plt.hist(v_list, bins=100)
plt.xlabel("v")

plt.show()
