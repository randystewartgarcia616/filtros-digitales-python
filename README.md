# Proyecto: filtros digitales
Diseño y evaluación de filtros pasa bajos, pasa altos y pasa bandas usando Python.

## Señal de prueba
Señal compuesta de 5, 50 y 120 Hz, muestreada a 1000 Hz durante 2 segundos, con ruido blanco añadido.

## Métodos
- IIR Butterworth de orden 6.
- FIR con ventana Hamming.
- Cortes: 20 Hz (pasa bajos), 80 Hz (pasa altos), 40–65 Hz (pasa bandas).

## Instalación
`pip install -r requirements.txt`

## Ejecución
`python filtros_digitales.py`

El programa muestra gráficas temporales y respuestas en frecuencia.
