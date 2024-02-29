# Removing the dependency on scipy.signal and defining the Hann window manually

import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
Fs = 1024  # Sampling frequency
T = 1.0 / Fs  # Sampling interval
L = 1024  # Length of the signal
t = np.arange(0, L) * T  # Time vector

# Signal with 100 zeroes, then 100 ones, then 100 zeroes
x = np.concatenate((np.zeros(100), np.ones(100), np.zeros(100), np.zeros(724)))

# Manually create a Hann window
hann_window = 0.5 - 0.5 * np.cos(2 * np.pi * np.arange(L) / L)

# Apply Hann window to the signal
x_windowed = x * hann_window

# FFT of the original signal
X = np.fft.fft(x)
X_magnitude = np.abs(X / L)
X_magnitude[1:L//2] *= 2

# FFT of the windowed signal
X_windowed = np.fft.fft(x_windowed)
X_windowed_magnitude = np.abs(X_windowed / L)
X_windowed_magnitude[1:L//2] *= 2

# Frequency axis
f = Fs * np.arange(0, (L/2)) / L

# Plot the frequency spectrum of both signals
plt.figure(figsize=(15, 5))

# Plot original signal spectrum
plt.subplot(1, 2, 1)
plt.plot(f, X_magnitude[:L//2], label='Original')
plt.title('Frekvens spekter uten Hann vindu')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('X_f')
plt.grid()
plt.legend()

# Plot windowed signal spectrum
plt.subplot(1, 2, 2)
plt.plot(f, X_windowed_magnitude[:L//2], label='Med Hann vindu', color='orange')
plt.title('Frequency Spectrum with Hann Window')
plt.xlabel('Frekvens [Hz]')
plt.ylabel('X_f')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
