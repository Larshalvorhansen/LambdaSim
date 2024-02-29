# Importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Signal parameters
Fs = 1024  # Sampling frequency
T = 1.0 / Fs  # Sampling interval
L = 1024  # Length of the signal

# Complex sinusoidal signal with a frequency of 0 (DC component)
x_complex = np.exp(-1j * 2 * np.pi * 0 * np.arange(L) * T)

# FFT of the complex signal and shift
X_complex = np.fft.fft(x_complex)
X_complex_shifted = np.fft.fftshift(X_complex)
X_complex_shifted_magnitude = np.abs(X_complex_shifted / L)
X_complex_shifted_magnitude *= 2  # Adjusting for normalization

# Frequency axis
f_shifted = np.fft.fftshift(np.fft.fftfreq(L, T))

# Plotting the frequency spectrum with spike at frequency = 0
plt.figure(figsize=(10, 5))
plt.plot(f_shifted, X_complex_shifted_magnitude, label='Forskjøvent kompleks sinus')
plt.title('forskjovet frekvens spekter')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('X(f)')
plt.grid()
plt.legend()
plt.show()
