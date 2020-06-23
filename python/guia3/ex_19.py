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
from scipy.signal import remez

# Sampling frequency
fs = 2.01


def get_M(ripple_l, ripple_h, w_l, w_h):
    num = -10 * math.log10(ripple_h * ripple_l) - 13
    den = 2.324 * abs(w_h - w_l)
    retval = int(math.ceil(num / den))
    if (retval % 2 != 0):
        retval += 1
    return retval


def desired_lowpass():

    ripple_low = 0.05
    ripple_high = 0.01
    # Normalized frequencies vector
    F = [0, 0.4, 0.50, 1]
    # Desired amplitudes of each point listed in 'F'
    Amp = [1, 0]
    # Weights vector
    W = [1/ripple_low, 1/ripple_high]

    M = get_M(ripple_low, ripple_high, 0.4, 0.5)

    h = remez(M+1, F, Amp, W, Hz=fs)
    A_w = get_amplitude_func(h, 1)

    plt.figure()
    plt.plot(h)
    plt.title("h[n] is GLP filter of type I.")
    plt.grid()
    plt.legend()

    w = np.linspace(-2 * math.pi, 2 * math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w /= math.pi

    plt.figure()
    plt.plot(w, A)
    plot_plus("A(w)")


def desired_highpass():

    ripple_low = 0.01
    ripple_high = 0.05
    # Normalized frequencies vector
    F = [0, 0.5, 0.6, 1]
    # Desired amplitudes of each point listed in 'F'
    Amp = [0, 1]
    # Weights vector
    W = [1/ripple_low, 1/ripple_high]

    M = get_M(ripple_low, ripple_high, 0.5, 0.6)

    h = remez(M+1, F, Amp, W, Hz=fs)
    A_w = get_amplitude_func(h, 1)

    plt.figure()
    plt.plot(h)
    plt.title("h[n] is GLP filter of type I.")
    plt.grid()
    plt.legend()

    w = np.linspace(-2 * math.pi, 2 * math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w /= math.pi

    plt.figure()
    plt.plot(w, A)
    plot_plus("A(w)")


def desired_bandpass():

    ripple_low = 0.02
    ripple_medium = 0.05
    ripple_high = 0.01
    # Normalized frequencies vector
    F = [0, 0.3, 0.4, 0.7, 0.8, 1]
    # Desired amplitudes of each point listed in 'F'
    Amp = [0, 1, 0]
    # Weights vector
    W = [1/ripple_low, 1/ripple_medium, 1/ripple_high]

    M = get_M(ripple_medium, ripple_high, 0.7, 0.8)

    h = remez(M+1, F, Amp, W, Hz=fs)
    A_w = get_amplitude_func(h, 1)

    plt.figure()
    plt.plot(h)
    plt.title("h[n] is GLP filter of type I.")
    plt.grid()
    plt.legend()

    w = np.linspace(-2 * math.pi, 2 * math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w /= math.pi

    plt.figure()
    plt.plot(w, A)
    plot_plus("A(w)")


def ex_19():
    desired_lowpass()
    desired_highpass()
    desired_bandpass()


def main():
    ex_19()


main()
