import numpy as np
import matplotlib.pyplot as plt
import rcparams
from numpy import pi, exp, sqrt, cos, sin
from numpy.random import normal, uniform

#n_walkers \t Dx \t Dy \t t_steps \t dt \t R \t R_w \t theta0 \t c_x \t c_y\n
n_walkers, Dx, Dy, t_steps, dt, R, R_w, theta0, c_x, c_y = np.loadtxt("info.txt", skiprows=1, unpack=True)

n_walkers = int(n_walkers)
Dx = float(Dx)
Dy = float(Dy)
t_steps = int(t_steps)
dt = float(dt)
R = float(R)
R_w = float(R_w)
theta0 = float(theta0)
c_x = float(c_x)
c_y = float(c_y)


print("n_walkers: ", n_walkers)
print("Dx: ", Dx)
print("Dy: ", Dy)
print("t_steps: ", t_steps)
print("dt: ", dt)
print("R: ", R)
print("R_w: ", R_w)
print("theta0: ", theta0)
print("c_x: ", c_x)
print("c_y: ", c_y)

###################################

# Read the walker positions from the file

data = np.loadtxt("walker_positions.txt", skiprows=1)

t_list = data[:, 0]
x_list = data[:, 1::2]
y_list = data[:, 2::2]

t_length_read = len(t_list)
print("{} time steps read from file".format(t_length_read))

# for t_i, t in enumerate(t_list):
#     print(t, end=" ")
#     for w_i in range(n_walkers):
#         x = x_list[t_i, w_i]
#         y = y_list[t_i, w_i]
#         print(x, y, end=" ")
#     print()

#####################################

fig, ax = plt.subplots(1, 1, figsize=(8, 8), constrained_layout=True)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

ax.set_xlim(-R - 0.1, R + 0.1)
ax.set_ylim(-R - 0.1, R + 0.1)
ax.set_aspect('equal', adjustable='box')

# Draw the circle
theta = np.linspace(0, 2 * pi, 100)
circle_x = R * cos(theta)
circle_y = R * sin(theta)
ax.plot(circle_x, circle_y, color='k', linewidth=2)

# Plot the final positions of the walkers
final_x_list = x_list[-1, :]
final_y_list = y_list[-1, :]
ax.scatter(final_x_list, final_y_list, color='blue', alpha=0.5, s=1)

# Mark the initial position of the walkers
w_i_x = R_w * cos(theta0) + c_x
w_i_y = R_w * sin(theta0) + c_y
ax.scatter(w_i_x, w_i_y, color='red', label='Initial Position', s=10)

# plt.savefig("final_positions.pdf", dpi=300)
plt.savefig("final_positions.png", dpi=300)
plt.clf()
plt.close()


#### Plot the histogram of final positions

fig, ax = plt.subplots(1, 1, figsize=(8, 8), constrained_layout=True)

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")

ax.set_xlim(-R - 0.1, R + 0.1)
ax.set_ylim(-R - 0.1, R + 0.1)
ax.set_aspect('equal', adjustable='box')

# Draw the circle
ax.plot(circle_x, circle_y, color='k', linewidth=2)

ax.hist2d(final_x_list, final_y_list, bins=100, range=[[-R, R], [-R, R]], cmap='hot', alpha=0.5, density=False)

# Mark the initial position of the walkers
ax.scatter(w_i_x, w_i_y, color='red', label='Initial Position', s=10)

# plt.savefig("final_positions_hist2d.pdf", dpi=300)
plt.savefig("final_positions_hist2d.png", dpi=300)

plt.clf()
plt.close()

## 3D histogram plot
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
ax.set_zlabel(r"$P(x,y)$")
ax.set_xlim(-R - 0.1, R + 0.1)
ax.set_ylim(-R - 0.1, R + 0.1)
ax.set_zlim(0, 1)
ax.set_box_aspect([1, 1, 1])  # Aspect ratio is 1:1:1

z = np.zeros_like((final_x_list, final_y_list))
xedges = np.linspace(-R, R, 100)
yedges = np.linspace(-R, R, 100)
hist, xedges, yedges = np.histogram2d(final_x_list, final_y_list, bins=100, range=[[-R, R], [-R, R]], density=True, weights=np.ones_like(final_x_list) / len(final_x_list))
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")
zpos = 0
dx = dy = 0.1
dz = hist.flatten()
dz = dz / dz.max()  # Normalize the histogram values for better visualization
# dz = dz / sum(dz)  # Normalize the histogram values for better visualization
# Create a 3D bar plot
ax.bar3d(xpos.flatten(), ypos.flatten(), zpos, dx, dy, dz, zsort='average', color=cm.hot(dz), alpha=0.5)
# Mark the initial position of the walkers
ax.scatter(w_i_x, w_i_y, color='red', label='Initial Position', s=10)
# plt.savefig("final_positions_hist3d.pdf", dpi=300)
plt.savefig("final_positions_hist3d.png", dpi=300)
# plt.show()

