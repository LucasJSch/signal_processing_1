#! /usr/bin/env python

"""
Se desea disenar un filtro pasa altos con las siguientes especificaciones:

|H(e^jw)|  <= 0.004             ,          0 <= |w| <= 0.18pi

0.94 <= |H(e^jw)| <= 1.06       ,          0.5pi <= |w| <= pi


Delta_p = 0.06
Delta_s = 0.004

--> Por simetria de las ventanas, requerimos delta <= 0.004

delta_w = 0.32pi
"""

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.amplitude_function import get_amplitude_func
from common.impulse_responses import ideal_highpass_truncated
from common.plot_utils import plot_plus


# According to the table, using a Hamming window with M ~= 26 will do the job.
def get_impulse_response(M):
    h_ideal = ideal_highpass_truncated(0.34*math.pi, M)
    window = np.hamming(M + 1)
    return np.multiply(h_ideal, window)


def ex_5():
    M = 25
    h = get_impulse_response(M)
    A_w = get_amplitude_func(h, 2)

    plt.figure()
    plt.plot(h)
    plt.title("Impulse response corresponds to a type II filter")
    plt.grid()
    plt.legend()

    plt.figure()
    w = np.linspace(-2 * math.pi, 2*math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w/= math.pi
    plt.plot(w, A)
    plot_plus(title="Freq. response", xlabel="$\omega/\pi$", ylabel="A($\omega$)")


def main():
    ex_5()


main()
