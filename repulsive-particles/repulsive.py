import numpy as np
import matplotlib.pyplot as plt
import rcparams

import numpy as np
import random

# Parameters
Lx, Ly = 10, 10                          # Lattice dimensions
phi = 0.5                               # Fraction of charges
n = int((Lx * Ly) * phi)                 # Number of charges
k1 = 1.0                                  # Constant for the potential
k2 = 0.05                                  # Constant for the potential
T_initial = 3.0                          # Initial temperature for annealing
T_final = 0.01                           # Final temperature
cooling_rate = 0.5                       # Cooling factor
max_iter = 1000                          # Iterations per temperature

# Distance function for periodic boundary conditions
def distance(p1, p2, Lx, Ly):
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    dx = min(dx, Lx - dx)  # Periodic boundary condition in x
    dy = min(dy, Ly - dy)  # Periodic boundary condition in y
    return np.sqrt(dx**2 + dy**2)

# Potential function (repulsive Coulomb-like)
def potential_energy(positions, Lx, Ly):
    energy = 0
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            r = distance(positions[i], positions[j], Lx, Ly)
            if r != 0:
                energy += k1 / r - (0.5) * (k2) * r**2
    return energy

# Random initial placement of charges
def initialize_positions(Lx, Ly, n):
    positions = set()
    while len(positions) < n:
        x, y = random.randint(0, Lx - 1), random.randint(0, Ly - 1)
        positions.add((x, y))
    return list(positions)

# Move a charge to a random nearby position
def random_move(position, Lx, Ly):
    x, y = position
    dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])
    new_x = (x + dx) % Lx
    new_y = (y + dy) % Ly
    return new_x, new_y

# Simulated Annealing
def simulated_annealing(positions, T_initial, T_final, cooling_rate, max_iter):
    T = T_initial
    current_energy = potential_energy(positions, Lx, Ly)

    while T > T_final:
        for _ in range(max_iter):
            i = random.randint(0, n - 1)
            new_position = random_move(positions[i], Lx, Ly)

            if new_position not in positions:
                # Test new configuration
                old_position = positions[i]
                positions[i] = new_position
                new_energy = potential_energy(positions, Lx, Ly)

                # Accept or reject new position based on energy difference
                delta_energy = new_energy - current_energy
                if delta_energy < 0 or random.uniform(0, 1) < np.exp(-delta_energy / T):
                    current_energy = new_energy
                else:
                    positions[i] = old_position

        # Cool down temperature
        T *= cooling_rate

    return positions, current_energy

# Run simulation
positions = initialize_positions(Lx, Ly, n)
initial_positions = positions.copy()
final_positions, final_energy = simulated_annealing(positions, T_initial, T_final, cooling_rate, max_iter)

print("Final potential energy:", final_energy)

plt.figure(figsize=(12, 6))

# Plot initial positions
plt.subplot(1, 2, 1)
plt.title("Initial configuration")

for x, y in initial_positions:
    plt.scatter(x, y, color='red', s=100)
    
plt.xlim(-1, Lx)
plt.ylim(-1, Ly)
plt.gca().set_aspect('equal', adjustable='box')
plt.xticks([])
plt.yticks([])
plt.grid(True)

# Plot final positions
plt.subplot(1, 2, 2)
plt.title("Final configuration")

for x, y in final_positions:
    plt.scatter(x, y, color='blue', s=100)
    
plt.xlim(-1, Lx)
plt.ylim(-1, Ly)
plt.gca().set_aspect('equal', adjustable='box')
plt.xticks([])
plt.yticks([])
plt.grid(True)

plt.tight_layout()

plt.savefig("simulated_annealing.pdf")