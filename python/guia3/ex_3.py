#! /usr/bin/env python

"""
Como se pudo apreciar en el ejercicio anterior, es posible disenar un filtro
de forma aproximada y ajustar el ancho de la banda de transicion variando el
orden del mismo.
Sin embargo, puede darse el caso en que los requerimientos del diseno exijan
una restriccion mayor en alguna de las bandas donde se especifique un ripple
menor al que podriamos lograr con una ventana rectangular.
Sabemos que los ripples producidos por el efecto de la ventana rectangular
estan relacionados con los lobulos secundarios de su respuesta en frecuencia.
Por lo tanto, parareducir el ripple podriamos buscar ventanas cuya respuesta
en frecuencia posea lobulos secundarios mas pequenos. Esto es posible si
elegimos una forma de ventana con bordes (alrededor de n = 0 y n = M) menos
abruptos que el caso de la ventana rectangular (donde existe una discontinuidad
en los extremos de la ventana). En este ejercicio vamos a explorar algunas de
las ventanas mas comunes y las diferencias entre ellas, estas son:
Rectangular, Bartlet, Hann, Hamming y Blackman.
"""

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs1
from common.impulse_responses import ideal_lowpass_truncated

nfft = 4 * 2048
M = 200


def get_windows():
    bartlett = np.bartlett(M)
    rectangular = np.ones(shape=M)
    blackman = np.blackman(M)
    hamming = np.hamming(M)
    hanning = np.hanning(M)

    return (bartlett, rectangular, blackman, hamming, hanning)


def fft_and_normalize_and_to_dB(window):
    window = fft(window, nfft)
    window /= window.max()
    window = np.absolute(window)
    20 * np.log10(window)
    return window


def get_fft_windows():
    (bartlett, rectangular, blackman, hamming, hanning) = get_windows()
    bartlett = fft_and_normalize_and_to_dB(bartlett)
    rectangular = fft_and_normalize_and_to_dB(rectangular)
    hamming = fft_and_normalize_and_to_dB(hamming)
    hanning = fft_and_normalize_and_to_dB(hanning)
    blackman = fft_and_normalize_and_to_dB(blackman)

    return (bartlett, rectangular, blackman, hamming, hanning)


# Compares the different window's curves as they tend to null values at the
# borders.
def ex_3_a():
    (bartlett, rectangular, blackman, hamming, hanning) = get_windows()

    plt.plot(bartlett, label="Bartlett")
    plt.plot(rectangular, label="Rectangular")
    plt.plot(blackman, label="Blackman")
    plt.plot(hamming, label="Hamming")
    plt.plot(hanning, label="Hann/Hanning")
    plt.title("Windows comparison with M=200")
    plt.legend()
    plt.grid()
    plt.show()


# Compares the main-vs-seconday lobes relationship between windows.
def ex_3_b():
    (bartlett, rectangular, blackman, hamming, hanning) = get_fft_windows()
    w = (np.arange(0, nfft) * 2 * math.pi / nfft) - math.pi

    plt.plot(w, bartlett, label="Bartlett")
    plt.plot(w, rectangular, label="Rectangular")
    plt.plot(w, blackman, label="Blackman")
    plt.plot(w, hamming, label="Hamming")
    plt.plot(w, hanning, label="Hann/Hanning")
    plt.title("Windows comparison in frequency with M=200")
    plt.legend()
    plt.grid()
    plt.show()


# Compares filtering with the window method using different windows
def ex_3_c():
    (bartlett, rectangular, blackman, hamming, hanning) = get_windows()
    w = (np.arange(0, nfft) * 2 * math.pi / nfft) - math.pi
    w_c = math.pi / 2
    h_ideal = ideal_lowpass_truncated(w_c, M-1)
    h_rectangular = fft_and_normalize_and_to_dB(h_ideal)
    h_blackman = fft_and_normalize_and_to_dB(np.multiply(h_ideal, blackman))
    h_bartlett = fft_and_normalize_and_to_dB(np.multiply(h_ideal, bartlett))
    h_hamming = fft_and_normalize_and_to_dB(np.multiply(h_ideal, hamming))
    h_hanning = fft_and_normalize_and_to_dB(np.multiply(h_ideal, hanning))

    plt.plot(w, h_bartlett, label="Bartlett")
    plt.plot(w, h_rectangular, label="Rectangular")
    plt.plot(w, h_blackman, label="Blackman")
    plt.plot(w, h_hamming, label="Hamming")
    plt.plot(w, h_hanning, label="Hann/Hanning")
    plt.title("Windows comparison in frequency with M=200")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    ex_3_c()


main()
