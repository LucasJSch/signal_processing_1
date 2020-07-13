#! /usr/bin/env python

# Python native libs
import math
import numpy as np
import control
import matplotlib.pyplot as plt
from scipy.signal import butter, freqs


# Project libs
from common.signal_utils import get_N_butterworth, get_w0_range_butterworth
from common.amplitude_function import get_amplitude_func
from common.plot_utils import plot_zpk_from_H

delta_p = 0.1
delta_s = 0.1
wp = 95.0
ws = 200.0


def ex_21():
    N = get_N_butterworth(delta_p, delta_s, wp, ws)
    w0 = np.ceil(min(get_w0_range_butterworth(delta_p, delta_s, wp, ws, N)))
    # Get coefficients
    (num, den) = butter(N, w0, btype='lowpass', analog=True, output='ba')
    # Get transfer system
    H = control.tf(num, den)

    # Plot freq. response
    w, h = freqs(num, den)
    plt.semilogx(w, 20 * np.log10(abs(h)))
    plt.title('Butterworth filter frequency response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude [dB]')
    plt.margins(0, 0.1)
    plt.grid(which='both', axis='both')
    plt.axvline(w0, color='green')  # cutoff frequency

    # Plot zeros-poles
    plot_zpk_from_H(H, title='Zeros-poles plot', w0=w0)
    plt.show()


def main():
    ex_21()


main()
