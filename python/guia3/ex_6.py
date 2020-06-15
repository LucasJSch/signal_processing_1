#! /usr/bin/env python

"""
Se desea disenar un filtro pasa banda mediante el metodo de ventanas.
Especificaciones:

       |H(e^jw)| <= 0.1              ,          0      <= |w| <= 0.15pi

0.9 <= |H(e^jw)| <= 1.1              ,          0.35pi <= |w| <= 0.6pi

       |H(e^jw)| <= 0.04             ,          0.75pi <= |w| <= pi

delta_1 = 0.1
delta_2 = 0.04

delta_w_1 = 0.2pi
delta_w_2 = 0.15pi

w_c_l = 0.25pi
w_c_h = 0.675pi
"""

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.amplitude_function import get_amplitude_func
from common.impulse_responses import ideal_bandpass_truncated
from common.plot_utils import plot_plus


# According to the table:
# First filter:  Bartlett, M1 = 40
# Second filter: Hann      M2 = 54
def get_impulse_response(M):
    h_ideal = ideal_bandpass_truncated(w_c_l=0.25*math.pi, w_c_h=0.675*math.pi, M=M)
    window = np.hanning(M + 1)
    return np.multiply(h_ideal, window)


def ex_6():
    M = 54
    h = get_impulse_response(M)
    A_w = get_amplitude_func(h, 1)

    plt.figure()
    plt.plot(h)
    plt.title("Impulse response corresponds to a type I filter")
    plt.grid()
    plt.legend()

    w = np.linspace(-1 * math.pi, math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w /= math.pi

    plt.figure()
    plt.plot(w, A)
    plot_plus("Freq. response")


def main():
    ex_6()


main()
