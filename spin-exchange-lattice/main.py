import numpy as np
import matplotlib.pyplot as plt
import rcparams

Lx, Ly = 32, 32

lattice = np.random.choice([-1, 1], size=(Lx, Ly), p=[0.5, 0.5])
# print("Initial lattice configuration:")
# print(lattice)

original_lattice = lattice.copy()

n_sweeps = 10000
T = 0.1

J = 1.0

def eight_neighbors(i, j, lattice):
    neighbors = []
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            x = (i + dx) % lattice.shape[0]
            y = (j + dy) % lattice.shape[1]
            neighbors.append((x, y))
    return neighbors

def energy(i, j, lattice, J):
    neighbors = eight_neighbors(i, j, lattice)
    E = 0
    for x, y in neighbors:
        E += -J * lattice[i, j] * lattice[x, y]
    return E

def monte_carlo_step(lattice, T, J):
    for i in range(lattice.shape[0]):
        for j in range(lattice.shape[1]):
            old_E = energy(i, j, lattice, J)
            this_site = lattice[i, j]
            
            new_lattice = lattice.copy()
            
            neighbors = eight_neighbors(i, j, new_lattice)
            random_neighbor_indx = np.random.choice(len(neighbors))
            random_neighbor_coords = neighbors[random_neighbor_indx]
            random_neighbor = (random_neighbor_coords[0], random_neighbor_coords[1])

            new_lattice[i, j], new_lattice[random_neighbor] = new_lattice[random_neighbor], new_lattice[i, j]
            new_E = energy(i, j, new_lattice, J)
            dE = new_E - old_E
            if dE < 0 or np.random.rand() < np.exp(-dE / T):
                lattice[i, j], lattice[random_neighbor] = lattice[random_neighbor], lattice[i, j]
            else:
                lattice[i, j] = this_site
    return lattice

sweep_counter = 0
for sweep in range(n_sweeps):
    lattice = monte_carlo_step(lattice, T, J)
    sweep_counter += 1
    percentage = (sweep_counter / n_sweeps) * 100
    if sweep_counter % 100 == 0 or sweep == n_sweeps - 1:
        print("{} / {} | {:.2f}%".format(sweep_counter, n_sweeps, percentage))

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].imshow(original_lattice, cmap='binary', interpolation='nearest')
ax[0].set_title('Initial Configuration')
ax[0].axis('off')

ax[1].imshow(lattice, cmap='binary', interpolation='nearest')
ax[1].set_title('Final Configuration')
ax[1].axis('off')

plt.tight_layout()

plt.savefig('lattice_evolution.png', dpi=300)