#! /usr/bin/env python

"""
Se desea disenar un filtro pasa bajos con las siguientes especificaciones:

0.98 <=  H(e^jw)  <= 1.02 ,          0 <= |w| <= 0.2pi

H(e^jw) <= 0.01           ,          0.3pi <= |w| <= pi


Delta_p = 0.02
Delta_s = 0.01

--> Por simetria de las ventanas, requerimos delta <= 0.01

delta_w = 0.1pi
"""

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs1
from common.amplitude_function import get_amplitude_func
from common.impulse_responses import ideal_lowpass_truncated
from common.plot_utils import plot_dense_freq_response, plot_plus


# According to the table, using a Hann window with M ~= 80 will do the job.
def get_impulse_response(M):
    h_ideal = ideal_lowpass_truncated(w_c=0.25*math.pi, M=M)
    window = np.hanning(M + 1)
    return np.multiply(h_ideal, window)


def ex_4():
    M = 75
    h = get_impulse_response(M)
    A_w = get_amplitude_func(h, 1)
    w = np.linspace(-1 * math.pi, math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    plt.figure()
    plt.plot(h)
    plt.title("Impulse response corresponds to a type I filter")
    plt.grid()
    plt.legend()
    plt.figure()
    plt.plot(w, A)
    plt.title("Freq. response")
    plot_dense_freq_response()


def main():
    ex_4()


main()
