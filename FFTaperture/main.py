import numpy as np
import matplotlib.pyplot as plt
from numpy import sin, exp, cos, pi, min, max, sqrt

x = np.zeros((1000, 1000))

a = 10
b = 5

i_thickness = 20
j_thickness = 20

i_mid = x.shape[0]//2
j_mid = x.shape[1]//2

for i in range(x.shape[0]):
    for j in range(x.shape[1]):
        r = sqrt((i-i_mid)**2 + (j-j_mid)**2)
        x[i, j] = exp(-((r-a)**2)/(2*b**2))

plt.figure(tight_layout=True)
plt.imshow(x, cmap='gray')
plt.colorbar()
# plt.show()
plt.savefig('plots/aperture.png')

print("Apeture constructed")


F = np.fft.fft2(x, norm='ortho')
F = np.roll(F, F.shape[0]//2, axis=0)
F = np.roll(F, F.shape[0]//2, axis=1)

plt.figure(tight_layout=True)
# plt.imshow(np.abs(F), cmap='hot')
plt.imshow(np.abs(F), cmap='gray', norm=plt.Normalize(vmin=0, vmax=1))
# plt.clim(0, 0.5)
plt.colorbar()
# plt.show()
plt.savefig('plots/Fourier.png')

print("Fourier transform done")
