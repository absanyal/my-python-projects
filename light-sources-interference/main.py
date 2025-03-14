import numpy as np
import matplotlib.pyplot as plt
import rcparams

from scipy.fftpack import fft2, ifft2, fftshift

from numpy import sqrt

def distance(source, target):
    s_x, s_y = source
    t_x, t_y = target
    return np.sqrt((s_x - t_x)**2 + (s_y - t_y)**2)

def wave(A, k, phi, source, target):
    r = distance(source, target)
    return A * np.sin(k * r + phi) / r


x = np.linspace(-50, 50, 1000)
y = np.linspace(-50, 50, 1000)

X, Y = np.meshgrid(x, y)

#-------------------------------------------------------------------------------------

# source_A = (0, 0)
# source_B = (0, 10)

# Amp_A = 10
# Amp_B = 10

# k_A = 1
# k_B = 1

# phi_A = 0
# phi_B = 0

# Z = wave(Amp_A, k_A, phi_A, source_A, (X, Y)) + wave(Amp_B, k_B, phi_B, source_B, (X, Y))

#-------------------------------------------------------------------------------------

num_pt_sources = 50

theta_source = np.linspace(0, 2*np.pi, num_pt_sources, endpoint=False)

Z = 0
for i in range(num_pt_sources):
    # R = 6
    # source_x = R * np.cos(theta_source[i])
    # source_y = R * np.sin(theta_source[i])
    source_x = np.random.uniform(min(x), max(x))
    source_y = np.random.uniform(min(y), max(y))
    Amp = 1
    k = 1
    phi = 0
    Z += wave(Amp, k, phi, (source_x, source_y), (X, Y))

#-------------------------------------------------------------------------------------

Z_intensity = Z**2

max_z = np.max(Z)
Z = Z / max_z

max_Z_intensity = np.max(Z_intensity)
Z_intensity = Z_intensity / max_Z_intensity

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].contourf(X, Y, Z, 100, cmap='jet')
ax[0].set_title('Wave')
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')

ax[1].contourf(X, Y, Z_intensity, 100, cmap='hot')
ax[1].set_title('Intensity')
ax[1].set_xlabel('x')
ax[1].set_ylabel('y')

plt.savefig('wave.png')