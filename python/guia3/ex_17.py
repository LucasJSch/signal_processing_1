#! /usr/bin/env python

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.signal_utils import fft_and_normalize_and_to_dB
from common.impulse_responses import diferentiator
from common.amplitude_function import get_amplitude_func
from common.plot_utils import plot_plus
from math import pi

M1 = 15
M2 = M1 + 1


def ex_17():
    h1 = diferentiator(M1)
    h2 = diferentiator(M2)
    A_w1 = get_amplitude_func(h1, 4)
    A_w2 = get_amplitude_func(h2, 3)

    plt.figure()
    plt.plot(h1)
    plt.title("h1[n] corresponds to type IV filter.")
    plt.grid()
    plt.legend()
    plt.figure()
    plt.plot(h2)
    plt.title("h2[n] corresponds to type III filter.")
    plt.grid()
    plt.legend()

    w = np.linspace(-2 * math.pi, 2 * math.pi, 4096)
    A1 = []
    A2 = []
    for i in w:
        A1.append(A_w1(i))
        A2.append(A_w2(i))
    w /= math.pi

    plt.figure()
    plt.plot(w, A1)
    plt.title("A1(w)")
    plt.grid()
    plt.legend()
    plt.figure()
    plt.plot(w, A2)
    plt.title("A2(w)")
    plt.grid()
    plt.legend()
    plt.show()


def main():
    ex_17()


main()
