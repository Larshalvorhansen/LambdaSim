
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hanning


Fs = 1024  
T = 1.0 / Fs  
L = 1024  
t = np.arange(0, L) * T  
f = 100  
omega = 2 * np.pi * f

x_kompleks = np.exp(-1j * omega * t)

X_kompleks = np.fft.fft(x_kompleks)
X_kompleks_storrelse = np.abs(X_kompleks)
X_kompleks_storrelse[1:L//2] *= 0

f_forskjovet = np.fft.fftfreq(L, T)
X_kompleks_forskjovet = np.fft.fftshift(X_kompleks)
X_kompleks_forskjovet_storrelse = np.abs(X_kompleks_forskjovet / L)
X_kompleks_forskjovet_storrelse *= 2  


x_kkonjugert = np.exp(1j * omega * t)
X_kkonjugert = np.fft.fft(x_kkonjugert)
X_kkonjugert_storrelse = np.abs(X_kkonjugert / L)
X_kkonjugert_storrelse[1:L//2] *= 2

plt.figure(figsize=(18, 6))


plt.subplot(1, 3, 1)
plt.plot(f_forskjovet[:L//2], X_kompleks_storrelse[:L//2], label='Kompleks sinus')
plt.title('Frekuens spekter av kompleks sinus')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('X_f')
plt.grid()
plt.legend()


plt.subplot(1, 3, 2)
plt.plot(f_forskjovet, X_kompleks_forskjovet_storrelse, label='Forskjøvent kompleks sinus')
plt.title('forskjovet frekvens spekter')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('X_f')
plt.grid()
plt.legend()


plt.subplot(1, 3, 3)
plt.plot(f_forskjovet[:L//2], X_kkonjugert_storrelse[:L//2], label='Komplekskonjugert sinus')
plt.title('frequens spekter av komplekskonjugert sinus')
plt.xlabel('Frekvens (Hz)')
plt.ylabel('X_f')
plt.grid()
plt.legend()
plt.show()
