import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
N = 100  # Number of beads
L = 10.0  # Bond length
k = 1.0  # Spring constant
d = 0.1  # Bending stiffness

# Initialize the positions of the beads
positions = np.zeros((N, 3))
positions[0] = np.array([0.0, 0.0, 0.0])

# Simulate the chain
for i in range(1, N):
    # Calculate the forces on the bead
    forces = np.zeros(3)
    for j in range(i):
        r = positions[i] - positions[j]
        forces += k * r / np.linalg.norm(r, keepdims=True)
    # Calculate the new position of the bead
    positions[i] = positions[i - 1] + L * forces / d

# Plot the chain
plt.plot(positions[:, 0], positions[:, 1])
plt.show()
