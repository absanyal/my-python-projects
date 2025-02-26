import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to normalize a vector


def normalize(v):
    return v / np.linalg.norm(v)

# Function to perform the Gram-Schmidt process to find orthonormal vectors


def gram_schmidt(v1, v2):
    # Project v2 onto v1
    projection = np.dot(v2, v1) * v1
    # Subtract projection from v2 to make it orthogonal to v1
    orthogonal_v2 = v2 - projection
    # Normalize both vectors
    f = normalize(orthogonal_v2)
    # Compute the cross product of v1 and f to get g
    g = np.cross(v1, f)
    # Normalize g
    g = normalize(g)
    return f, g

# Main function to find orthonormal vectors f and g given h


def find_orthonormal_vectors(h):
    # Normalize h
    h_norm = normalize(h)

    # Choose an arbitrary vector not parallel to h_norm
    # If h_norm is (1,0,0), pick (0,1,0), for example.
    if np.allclose(h_norm, [1, 0, 0]):
        arbitrary_vector = np.array([0, 1, 0])
    else:
        arbitrary_vector = np.array([1, 0, 0])

    # Apply Gram-Schmidt to get f and g
    f, g = gram_schmidt(h_norm, arbitrary_vector)

    return h_norm, f, g


def format_array(arr):
    return np.array2string(arr, formatter={'float_kind': lambda x: "%.2f" % x})


# Example usage:
h = np.array([-1, -2, 1])  # Example arbitrary vector h
h_norm, f, g = find_orthonormal_vectors(h)

# Plotting h, f, g in a 3D space
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
ax.quiver(0, 0, 0, h_norm[0], h_norm[1], h_norm[2], color='r', label='h')
ax.quiver(0, 0, 0, f[0], f[1], f[2], color='g', label='f')
ax.quiver(0, 0, 0, g[0], g[1], g[2], color='b', label='g')

# Plot the x, y, z axes
ax.quiver(0, 0, 0, 1, 0, 0, color='k', linestyle='dashed', label='x-axis')
ax.quiver(0, 0, 0, 0, 1, 0, color='k', linestyle='dashed', label='y-axis')
ax.quiver(0, 0, 0, 0, 0, 1, color='k', linestyle='dashed', label='z-axis')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set the limits of the plot
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Add a legend
ax.legend()

# Show the plot
plt.show()
