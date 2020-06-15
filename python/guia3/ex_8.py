#! /usr/bin/env python

"""
Implemente un filtro pasa bajos con frecuencia de corte  w_c = pi/2 y orden M = 50 usando
una ventana de Kaiser para distintos valores del parametro beta (por ejemplo: 0, 1, 2, 3 y 4 ).
"""

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.signal_utils import fft_and_normalize_and_to_dB
from common.impulse_responses import ideal_lowpass_truncated
from common.kaiser_utils import get_kaiser_window
from common.plot_utils import plot_plus

M = 50
w_c = math.pi / 2
nfft = 4 * 2048


def a():
    for beta in np.linspace(0, 10, endpoint=True, num=8):
        h = np.kaiser(M + 1, beta)
        plt.plot(h, label="Beta = " + str(beta))
    plot_plus(title="Kaiser windows comparison with fixed M = " + str(M), xlabel="n", ylabel="h[n]")


def b():
    w = (np.arange(0, nfft) * 2 * math.pi / nfft) - math.pi
    w /= math.pi
    for beta in np.linspace(0, 10, endpoint=True, num=8):
        h = np.kaiser(M + 1, beta)
        plt.plot(w, fft_and_normalize_and_to_dB(h, nfft), label="Beta = " + str(beta))
    plot_plus(title="FFT Kaiser windows comparison with fixed M = " + str(M), xlabel="w", ylabel="H[(e^jw) [dB]")


def main():
    a()
    b()


main()
