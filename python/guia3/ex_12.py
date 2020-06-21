#! /usr/bin/env python

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.signal_utils import fft_and_normalize_and_to_dB
from common.impulse_responses import ideal_multiband_truncated
from common.amplitude_function import get_amplitude_func
from common.plot_utils import plot_plus
from math import pi

ripple = 0.005
M = 160

freqs = [0.175*pi, 0.375*pi, 0.575*pi, 0.825*pi]
gains = [0, 1.5, 0, 0.75, 0]


def ex_12():
    window = np.hamming(M+1)
    h_ideal = ideal_multiband_truncated(gains, freqs, M)
    h = np.multiply(h_ideal, window)
    A_w = get_amplitude_func(h, 1)

    plt.figure()
    plt.plot(h, label="h[n]")

    w = np.linspace(-1 * math.pi, math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w /= math.pi

    plt.figure()
    plt.plot(w, A)
    plot_plus("Freq. response")


def main():
    ex_12()


main()
