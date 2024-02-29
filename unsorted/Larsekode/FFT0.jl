using Plots
using FFTW

# Original signal parameters
Fs = 1024 * 2  # Sampling frequency (Hz)
T = 1 / Fs     # Sample time (s)
L_original = 1024  # Original length of the sine part of the signal
t = 0:T:(L_original-1)*T  # Time vector

# Signal with sine values
x_sine = sin.(100 * 2 * π * t)

# Append 3072 zeroes to the signal
x = vcat(x_sine, 1)
w = vcat(zeros(100), ones(824), zeros(100))

# New length of the signal after appending zeroes
L = length(x)

# FFT
X = fft(x)
P2 = abs.(X/L)
P1 = P2[1:L÷2+1]
P1[2:end-1] *= 2

# Frequency axis
f = Fs * (0:(L÷2)) / L

# Limit the plot to 0 to 200 Hz
limit_index = findfirst(f -> f > 200, f)  # Correct the search within f
f_limited = f[1:limit_index-1]  # Limit the frequency range to 0-200 Hz
P1_limited = P1[1:limit_index-1]  # Limit the power spectrum data to the same range

# Plot
plot(f_limited, P1_limited, label="X(f)", xlabel="frekvens (Hz)", ylabel="X_f størrelse", title="Frekvens spekter for x(t)", xlims=(0, 200))
print(w)
print(x_sine)