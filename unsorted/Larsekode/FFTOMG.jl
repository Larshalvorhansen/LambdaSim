using Plots
using FFTW

# Signal parameters
Fs = 1024*2  # Sampling frequency (Hz)
T = 1/Fs   # Sample time (s)
L = 1024  # Length of the signal (number of samples)
t = 0:T:L*T-T  # Time vector

# Signal
x = sin.(100*2 * π * t)

# FFT
X = fft(x)
P2 = abs.(X/L)
P1 = P2[1:L÷2+1]
P1[2:end-1] *= 2

# Frequency axis
f = Fs * (0:(L÷2))/L

# Plot
plot(f, P1, label="X(f)", xlabel="frekvens (Hz)", ylabel="X_f størrelse", title="Frekvens spekter for x(t)")
print("hei")