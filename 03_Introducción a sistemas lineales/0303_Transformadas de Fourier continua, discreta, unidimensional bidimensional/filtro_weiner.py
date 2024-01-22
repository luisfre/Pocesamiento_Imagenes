#Descripción del problema: Se desea aplicar un filtro basado en la transformada de Fourier
#Objetivo: Aplicar la transformada de Fourier mediante el filtro de Wiener
#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

N = 8129  # número de muestras
M = 256  # longitud del filtro de Wiener 
Om0 = 0.1*np.pi  # Frecuencia de la señal original
N0 = 0.1 #Densidad espectral de potencia 

# Generamos la señal original
s = np.cos(Om0 * np.arange(N))
# Generamos la señal observada
g = 1/20*np.asarray([1, 2, 3, 4, 5, 4, 3, 2, 1])
n = np.random.normal(size=N, scale=np.sqrt(N0))
x = np.convolve(s, g, mode='same') + n

f, Pxx = sig.csd(x, x, nperseg=M)
f, Psx = sig.csd(s, x, nperseg=M)
# Calculamos el filtro de Wiener
H = Psx/Pxx
H = H * np.exp(-1j*2*np.pi/len(H)*np.arange(len(H))*(len(H)//2)) 
h = np.fft.irfft(H)
# Aplicamos el filtro Wiener 
y = np.convolve(x, h, mode='same')

# Dibujamos
Om = np.linspace(0, np.pi, num=len(H))

plt.figure(figsize=(10, 4))
plt.subplot(121)
plt.plot(Om, 20*np.log10(np.abs(.5*Pxx)), label=r'$| \Phi_{xx}(e^{j \Omega}) |$ in dB')
plt.plot(Om, 20*np.log10(np.abs(.5*Psx)), label=r'$| \Phi_{sx}(e^{j \Omega}) |$ in dB')
plt.title('(Cross) PSDs')
plt.xlabel(r'$\Omega$')
plt.legend()
plt.axis([0, np.pi, -60, 40])
plt.grid()

# función de transferencia de trama del filtlro Wiener
plt.subplot(122)
plt.plot(Om, 20*np.log10(np.abs(H)))
plt.title('Transfer function of Wiener filter')
plt.xlabel(r'$\Omega$')
plt.ylabel(r'$| H(e^{j \Omega}) |$ in dB')
plt.axis([0, np.pi, -150, 3])
plt.grid()
plt.tight_layout()

# Dibujamos las señales
idx = np.arange(500, 600)
plt.figure(figsize=(10, 4))
plt.plot(idx, x[idx], label=r'observed signal $x[k]$')
plt.plot(idx, s[idx], label=r'original signal $s[k]$')
plt.plot(idx, y[idx], label=r'estimated signal $y[k]$')
plt.title('Signals')
plt.xlabel(r'$k$')
plt.axis([idx[0], idx[-1], -1.5, 1.5])
plt.legend()
plt.grid()
plt.show()