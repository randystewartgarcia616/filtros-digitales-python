"""Actividad formativa 3: filtros digitales FIR e IIR."""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Señal compuesta de 5, 50 y 120 Hz con ruido blanco
fs = 1000
t = np.arange(0, 2, 1/fs)
rng = np.random.default_rng(42)
limpia = (np.sin(2*np.pi*5*t) + 0.7*np.sin(2*np.pi*50*t)
          + 0.5*np.sin(2*np.pi*120*t))
entrada = limpia + 0.45*rng.normal(size=len(t))

# Diseño de filtros IIR Butterworth y FIR con ventana Hamming
filtros = {
 "Pasa bajos IIR": ("IIR", signal.butter(6, 20, btype="lowpass", fs=fs, output="sos")),
 "Pasa altos IIR": ("IIR", signal.butter(6, 80, btype="highpass", fs=fs, output="sos")),
 "Pasa bandas IIR": ("IIR", signal.butter(6, [40,65], btype="bandpass", fs=fs, output="sos")),
 "Pasa bajos FIR": ("FIR", signal.firwin(101, 20, fs=fs, window="hamming")),
 "Pasa altos FIR": ("FIR", signal.firwin(101, 80, fs=fs, pass_zero=False, window="hamming")),
 "Pasa bandas FIR": ("FIR", signal.firwin(151, [40,65], fs=fs, pass_zero=False, window="hamming"))
}

# Aplicación y visualización
for nombre, (tipo, coef) in filtros.items():
    if tipo == "IIR":
        salida = signal.sosfiltfilt(coef, entrada)
        f, h = signal.sosfreqz(coef, worN=2048, fs=fs)
    else:
        salida = signal.filtfilt(coef, [1.0], entrada)
        f, h = signal.freqz(coef, [1.0], worN=2048, fs=fs)

    fig, ax = plt.subplots(2, 1, figsize=(9, 5))
    ax[0].plot(t, entrada, label="Entrada con ruido", alpha=.45)
    ax[0].plot(t, salida, label="Salida filtrada")
    ax[0].set_xlim(0, .5)
    ax[0].set_xlabel("Tiempo (s)")
    ax[0].set_title(nombre + " - comparación temporal")
    ax[0].legend(); ax[0].grid()
    ax[1].plot(f, 20*np.log10(np.maximum(np.abs(h), 1e-8)))
    ax[1].set_xlim(0, 200); ax[1].set_ylim(-100, 5)
    ax[1].set_xlabel("Frecuencia (Hz)")
    ax[1].set_ylabel("Magnitud (dB)")
    ax[1].set_title("Respuesta en frecuencia")
    ax[1].grid()
    fig.tight_layout()
    fig.savefig(nombre.lower().replace(" ", "_") + ".png", dpi=150)
    plt.show()
