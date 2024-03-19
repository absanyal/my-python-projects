import numpy as np
import matplotlib.pyplot as plt

decay_chance = 0.1

total = 1000000
target_percentage = 0.01

t_max = 500

t_interval = 1

t_list = []
atoms_list = []
decay_list = []

halflife_reached = 0

current_num = total

t = 0

percentage = 100 * current_num / total
print("t = {} : {} atoms left. ({:.2f} %)".format(t, current_num, percentage))

while (current_num > target_percentage * total and t < t_max):
    t += 1
    decays = 0
    for atom in range(current_num):
        r = np.random.uniform(0, 1)
        if r < decay_chance:
            decays += 1

    current_num -= decays

    if (halflife_reached == 0):
        if current_num <= total / 2:
            halflife_reached = 1
            print("Half-life reached at t =", t,
                  "seconds.", current_num, "atoms left.")

    # if (t % t_interval == 0):
    percentage = 100 * current_num / total
    print("t = {} : {} atoms left. ({:.2f} %)".format(t, current_num, percentage))


    atoms_list.append(current_num)
    decay_list.append(decays)
    t_list.append(t)

print("Ending simulation at t =", t, "seconds.", current_num, "atoms left.")

plt.figure(tight_layout=True)

plt.plot(t_list, atoms_list, 'o-', label="Atoms left", markersize=2)
plt.plot(t_list, decay_list, 'o-', label="Decays", markersize=2)

plt.xlabel("Time (s)")
plt.ylabel("Number of atoms")
plt.title("Radioactivity Simulation")
plt.grid(True)
plt.legend()
plt.savefig("radioactivity.pdf", dpi=300)
plt.show()
