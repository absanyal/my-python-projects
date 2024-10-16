import numpy as np
import matplotlib.pyplot as plt
from numpy import cross, dot, sin, cos, pi, exp
from numpy.linalg import norm
import matplotlib.animation

# from matplotlib.animation import FuncAnimation


def generate_orthogonal_vectors(h):

    h_x, h_y, h_z = h

    if h_x != 0 and h_y == 0 and h_z == 0:
        # h is along the x-axis
        f = (0, 1, 0)
        g = (0, 0, 1)
    elif h_x == 0 and h_y != 0 and h_z == 0:
        # h is along the y-axis
        f = (0, 0, 1)
        g = (1, 0, 0)
    elif h_x == 0 and h_y == 0 and h_z != 0:
        # h is along the z-axis
        f = (1, 0, 0)
        g = (0, 1, 0)
    else:
        # General case
        if h_x != 0 or h_y != 0 or h_z != 0:
            e_x = (1, 0, 0) if not (h_x == 1 and h_y ==
                                    0 and h_z == 0) else (0, 1, 0)
            f = cross(h, e_x)
            f = f / norm(f)
            g = cross(h, f)
            g = g / norm(g)

    return f, g


# h = [0, 0.1, 1.0]

# h = np.array(h)
# h = h / np.linalg.norm(h)

# f, g = generate_orthogonal_vectors(h)

# print('h = [{:.2f}, {:.2f}, {:.2f}]'.format(*h))
# print('f = [{:.2f}, {:.2f}, {:.2f}]'.format(*f))
# print('g = [{:.2f}, {:.2f}, {:.2f}]'.format(*g))

# print()

# print('h.f = {:.2f}'.format(np.dot(h, f)))
# print('f.g = {:.2f}'.format(np.dot(f, g)))
# print('g.h = {:.2f}'.format(np.dot(h, g)))

# print()

# print('h.h = {:.2f}'.format(np.dot(h, h)))
# print('f.f = {:.2f}'.format(np.dot(f, f)))
# print('g.g = {:.2f}'.format(np.dot(g, g)))

# print()

# print('h x f = [{:.2f}, {:.2f}, {:.2f}]'.format(*np.cross(h, f)))
# print('f x g = [{:.2f}, {:.2f}, {:.2f}]'.format(*np.cross(f, g)))
# print('g x h = [{:.2f}, {:.2f}, {:.2f}]'.format(*np.cross(g, h)))

# print()

# print('h x h = [{:.2f}, {:.2f}, {:.2f}]'.format(*np.cross(h, h)))
# print('f x f = [{:.2f}, {:.2f}, {:.2f}]'.format(*np.cross(f, f)))
# print('g x g = [{:.2f}, {:.2f}, {:.2f}]'.format(*np.cross(g, g)))

fig, ax = plt.subplots(subplot_kw={'projection': '3d'}, figsize=(
    5, 5), constrained_layout=True)
t_list = np.linspace(0, 2*np.pi, 1000, endpoint=True)


def update(frame):
    ax.clear()
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    t = frame

    theta = 1*t
    phi = 1*t

    hx = cos(theta)
    hy = sin(theta)
    hz = 0

    h = np.array([hx, hy, hz])
    h = h / np.linalg.norm(h)

    f, g = generate_orthogonal_vectors(h)

    ax.quiver(0, 0, 0, *h, color='r', label='h')
    ax.quiver(0, 0, 0, *f, color='g', label='f')
    ax.quiver(0, 0, 0, *g, color='b', label='g')

    ax.legend()


# ani = FuncAnimation(fig, update, frames=t_list, interval=1000/60)
ani = matplotlib.animation.FuncAnimation(
    fig, update, frames=t_list, interval=1000/60)

plt.show()
