#! /usr/bin/env python

"""
Ahora se desea disenar filtros con la ventana Kaiser.

Se desea disenar un filtro pasa bajos con las siguientes especificaciones:

0.98 <=  |H(e^jw)|  <= 1.02 ,          0 <= |w| <= 0.2pi

|H(e^jw)| <= 0.01           ,          0.3pi <= |w| <= pi


ripple = 0.01
delta_w = 0.05pi
"""

# Python native libs
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import fft

# Project libs
from common.amplitude_function import get_amplitude_func
from common.impulse_responses import ideal_lowpass_truncated
from common.kaiser_utils import get_kaiser_window
from common.plot_utils import plot_plus

ripple = 0.01
delta_w = 0.05 * math.pi
w_c = 0.25 * math.pi


def ex_7():
    (M, window) = get_kaiser_window(ripple, delta_w)
    # We know that h is simmetric.
    # Therefore, it depends on M whether its a type I or II filter.
    # k indicates the frequency range to take into account.
    if(M % 2 == 0):
        filter_type = 1
        k = 1
    else:
        filter_type = 2
        k = 2
    h_ideal = ideal_lowpass_truncated(w_c, M)
    h = np.multiply(h_ideal, window)
    A_w = get_amplitude_func(h, filter_type)

    plt.figure()
    plt.plot(h_ideal)
    plt.title("Impulse response corresponds to a type " + str(filter_type) + " filter.")
    plt.grid()

    plt.figure()
    w = np.linspace(-k*math.pi, k*math.pi, 4096)
    A = []
    for i in w:
        A.append(A_w(i))
    w /= math.pi
    plt.plot(w, A)
    plot_plus(title="Freq. response")


def main():
    ex_7()


main()
