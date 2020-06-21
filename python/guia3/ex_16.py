#! /usr/bin/env python

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.signal_utils import fft_and_normalize_and_to_dB
from common.impulse_responses import ideal_hilbert_transformer_truncated
from common.amplitude_function import get_amplitude_func
from common.plot_utils import plot_plus
from math import pi

ripple = 0.06
delta_omega = 0.1 * pi
M = 81
window = np.hanning(M+1)


def ex_16():
    h_ideal = ideal_hilbert_transformer_truncated(M)
    h = np.multiply(h_ideal, window)
    A_w = get_amplitude_func(h, 4)

    plt.figure()
    plt.plot(h)
    plt.title("h[n] corresponds to type III filter.")
    plt.grid()
    plt.legend()

    w = np.linspace(-2 * math.pi, 2 * math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w /= math.pi

    plt.figure()
    plt.plot(w, A)
    plot_plus("Freq. response")


def main():
    ex_16()


main()
