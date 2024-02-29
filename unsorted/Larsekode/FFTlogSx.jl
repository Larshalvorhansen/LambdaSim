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
P2 = 10 * log10.(S / L)  # Convert power to dB

# Normalize to the max value being 0 dB
max_value = maximum(P2)
P2 = P2 .- max_value

# Limit the plot to 0 to 200 Hz
limit_index = findfirst(f -> f > 200, Fs * (0:(L÷2)) / L)
f = Fs * (0:(limit_index-1)) / L
P2 = P2[1:limit_index]

# Plot
plot(f, P2, label="Sₓ(f)", xlabel="frekvens (Hz)", ylabel="Relativ effekt, [dB]", title="Effektspekteret til x(t) i", ylims=(-80, 10))
