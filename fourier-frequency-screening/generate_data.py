import numpy as np
from modules.seriessum import series_sum
import matplotlib.pyplot as plt
from numpy import pi, exp

t = np.linspace(-2*pi, 2*pi, 1000)
a = 20
n = 4

signal = np.zeros_like(t)
for i, x_val in enumerate(t):
    signal[i] = series_sum(a, n, x_val)
    # signal[i] = exp(- x_val**2)

f_signal = np.fft.rfft(signal)

W = np.fft.rfftfreq(len(signal), d=(2*pi)/len(signal))

cut_f_signal = f_signal.copy()
for i in range(len(W)):
    if 0 < W[i] < 1:
        cut_f_signal[i] *= 0.5

cut_signal = np.fft.irfft(cut_f_signal)

fig, ax = plt.subplots(1, 3, figsize=(15, 5), tight_layout=True)

ax[0].plot(t, signal)
ax[0].set_title('Original Signal')

ax[1].plot(W, np.abs(f_signal), label='Original Fourier Transform')
ax[1].set_title('Fourier Transform')
ax[1].plot(W, np.abs(cut_f_signal), label='Filtered Fourier Transform')
ax[1].set_title('Filtered Fourier Transform')
ax[1].legend()

ax[2].plot(t, signal, label='Original Signal', alpha=0.3)
ax[2].plot(t, cut_signal)
ax[2].set_title('Filtered Signal')


plt.show()