#! /usr/bin/env python

"""
Se requiere implementar un filtro FIR del tipo notch que cumpla con lo
siguiente:

0.95  |H(e^jw)|  <= 1.05  ,       0 <=    |w| <= 0.5pi

|H(e^jw)|  <= 0.005       ,               |w| = 0.6pi

0, 95  |H(e^jw)|  <= 1.05 ,       0.7pi < |w| < pi


ripple = 0.005

delta_w = 0.05pi

w_c_l = 0.55pi
w_c_h = 0.65pi
"""

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.signal_utils import fft_and_normalize_and_to_dB
from common.impulse_responses import ideal_notch_truncated
from common.amplitude_function import get_amplitude_func
from common.plot_utils import plot_plus

# According to the Table 1, a Hamming window with M=160 will work.
# This can be acheived *maybe* more efficiently by composing the filter with a
# lowpass + highpass, and use a different window for each one.
w_c_l = 0.55 * math.pi
w_c_h = 0.65 * math.pi
nfft = 4*2048
M = 160


def get_impulse_response(M):
    h_ideal = ideal_notch_truncated(w_c_l, w_c_h, M)
    window = np.hamming(M + 1)
    return np.multiply(h_ideal, window)


def ex_9():
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
    ex_9()


main()
