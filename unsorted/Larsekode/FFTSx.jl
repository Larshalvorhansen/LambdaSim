using Plots
using FFTW

# Signal parameters
Fs = 5000 * 2  # Sampling frequency (Hz)
T = 1 / Fs     # Sample time (s)
L = 1024       # Length of the signal (number of samples)
t = 0:T:(L-1)*T  # Time vector

# Signal
x = sin.(100 * 2 * π * t)

# FFT
X = fft(x)
S = abs.(X).^2  # Power spectrum is the square of the magnitude of the FFT
P2 = S / L
P1 = P2[1:L÷2+1]
P1[2:end-1] *= 2  # Compensate for energy at negative frequencies

# Frequency axis
f = Fs * (0:(L÷2)) / L

# Plot
plot(f, P1, label="Sₓ(f)", xlabel="frekvens (Hz)", ylabel="Effekt", title="Effektspekteret til x(t)")
