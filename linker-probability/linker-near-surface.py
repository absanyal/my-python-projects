import numpy as np
import matplotlib.pyplot as plt

T = 1
beta = 1/T

E = -1.6


class linkers:
    def __init__(self, N):
        self.N = N
        self.links = np.zeros(N)
        self.accepted = 0
        self.attempts = 0
        self.E = 0

    def get_energy(self, persite=False):
        energy = 0
        for i in range(self.N):
            energy += self.links[i] * E
        if (persite):
            energy /= self.N
        return energy

    def flip(self, i):
        if self.links[i] == 0:
            self.links[i] = 1
        elif self.links[i] == 1:
            self.links[i] = 0
        self.E = self.get_energy()

    def metropolis(self):
        for i in range(self.N):
            self.attempts += 1
            oldE = self.E
            self.flip(i)
            dE = self.E - oldE
            if dE >= 0:
                if np.random.rand() > np.exp(-beta*dE):
                    self.flip(i)
            else:
                self.accepted += 1

    def get_acceptance(self):
        return self.accepted/self.attempts

    def get_linked(self):
        return sum(self.links)


N = 50

f = linkers(N)

linked = []

nsteps = 50000

# bins_list = np.arange(0, N+1, 1)

with  open('linker-near-surface-time.txt', 'w') as data:
    
    for i in range(nsteps):
        f.metropolis()
        if i % 500 == 0:
            print("{:5.0f} E/N = {:+.2f} L = {:3.0f} A = {:.2f}".format(i,
                f.get_energy()/f.N, f.get_linked(), f.get_acceptance()))
        data.write("{:3.0f}\n".format(f.get_linked()))
