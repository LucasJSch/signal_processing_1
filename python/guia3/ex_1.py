#! /usr/bin/env python

""" Grafique la funcion amplitud A(w) del filtro truncado (puede utilizar la
funcion implementada en el ejercicio 6 de la Guia 2) superpuesta a la amplitud
deseada Ad(w) para comparar y observar el efecto producido en frecuencia debido
al truncamiento en el tiempo.
Utilice para la simulacion un vector de frecuencias w de por lo menos 2048
puntos. """


# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt

# Project libs
from common.amplitude_function import get_amplitude_func


def ex_1():
    # Cutoff frequency
    w_c = math.pi / 2
    # Frequency domain
    w = np.linspace(-1 * math.pi, math.pi, 4096)
    # Phase delay variations
    for M in [10, 100, 1000]:
        # Index of truncated sinc function
        n_trunc = np.linspace(0, M, endpoint=True, num=M+1)
        # Impulse response of truncated sinc function
        h_trunc = (w_c / math.pi) * np.sinc((w_c / math.pi) * (n_trunc - M/2))
        # Amplitude function of truncated sinc function
        A_w_trunc = get_amplitude_func(h_trunc, 1)

        y_trunc = []
        for i in w:
            y_trunc.append(A_w_trunc(i))

        plt.plot(w, y_trunc, label="M = " + str(M))

    y_ideal = [0] * 4096
    for i in xrange(1024, 3072):
        y_ideal[i] = 1

    plt.plot(w, y_ideal, label="Ideal frequency response")
    plt.title("Amplitude function of truncated sinc")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    ex_1()


main()
