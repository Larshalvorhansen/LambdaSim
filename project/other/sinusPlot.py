import numpy as np
import matplotlib.pyplot as plt

# Gjenoppretter de nødvendige variablene og konstantene
amplitude = 1  # Amplitude i Volt
frekvens = 100  # Frekvens i Hz
delta_t = 0.0002  # Samplingstid i sekunder
antall_punkter = 900  # Antall punkter i tidsvektoren
tidsvektor = np.arange(0, antall_punkter * delta_t, delta_t)
sinussignal = amplitude * np.sin(2 * np.pi * frekvens * tidsvektor)

# Tidsperiode vi ønsker å plotte (i sekunder)
onsket_tid = 0.18

# Beregner antall punkter for den ønskede tidsperioden
antall_punkter_onsket_tid = int(onsket_tid / delta_t)

# Plotter sinussignalet for den ønskede tidsperioden
plt.figure(figsize=(10, 6))
plt.plot(tidsvektor[:antall_punkter_onsket_tid], sinussignal[:antall_punkter_onsket_tid], label="x(t)")
plt.title("x(t) som funksjon av tid")
plt.xlabel("tid (s)")
plt.ylabel("amplitude (V)")
plt.grid(True)
plt.legend()
plt.savefig("oppg1.jpg")
plt.show()

