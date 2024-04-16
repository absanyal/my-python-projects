from matplotlib import tight_layout
import numpy as np
import matplotlib.pyplot as plt

pop, food = np.loadtxt('data/data.txt', unpack=True)

plt.figure(tight_layout=True)

plt.plot(pop, label='Population')
plt.plot(food, label='Food')

plt.xlabel('Time')

plt.legend()

plt.savefig("plots/pop.pdf")

plt.clf()
plt.cla()

eat, move, reproduce = np.loadtxt('data/gene.txt', unpack=True)

plt.figure(tight_layout=True)

plt.plot(eat, label='Eat')
plt.plot(move, label='Move')
plt.plot(reproduce, label='Reproduce')

plt.xlabel('Time')
plt.ylabel('Gene prevalence')

# plt.ylim(0, 1)

plt.legend()
plt.savefig("plots/gene.pdf")