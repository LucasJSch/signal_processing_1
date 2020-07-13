#! /usr/bin/env python

# Python native libs
import math
import numpy as np
import control
import matplotlib.pyplot as plt
from scipy.signal import butter, freqs, cheby1, cheby2, ellip
from math import pi

# Project libs
from common.signal_utils import get_N_butterworth, get_w0_range_butterworth
from common.plot_utils import plot_zpk_from_H

N = 5
delta_p = 0.1
delta_s = 0.2
fc = 112  # Hz
fp = 89   # Hz
fs = 134  # Hz
Ap = -20*math.log10(1 - delta_p)
As = -20*math.log10(delta_s)
Wc = 2*pi*fc
Wp = 2*pi*fp
Ws = 2*pi*fs


def ex_24():
    [b_butter, a_butter] = butter(N, Wc, analog=True)
    H = control.tf(b_butter, a_butter)
    plot_zpk_from_H(H, title='Zeros-poles plot for Butterworth filter')

    [b_ch1, a_ch1] = cheby1(N, Ap, Wp, analog=True)
    H = control.tf(b_ch1, a_ch1)
    plot_zpk_from_H(H, title='Zeros-poles plot for Chebyshev-I filter')

    [b_ch2, a_ch2] = cheby2(N, As, Ws, analog=True)
    H = control.tf(b_ch2, a_ch2)
    plot_zpk_from_H(H, title='Zeros-poles plot for Chebyshev-II filter')

    [b_elip, a_elip] = ellip(N, Ap, As, Wp, analog=True)
    H = control.tf(b_elip, a_elip)
    plot_zpk_from_H(H, title='Zeros-poles plot for elliptical filter')

    plt.figure()
    w_butter, h_butter = freqs(b_butter, a_butter)
    w_ch1, h_ch1 = freqs(b_ch1, a_ch1)
    w_ch2, h_ch2 = freqs(b_ch2, a_ch2)
    w_elip, h_elip = freqs(b_elip, a_elip)
    plt.plot(w_butter, abs(h_butter), label="Butterworth")
    plt.plot(w_ch1, abs(h_ch1), label="Chebyshev-I")
    plt.plot(w_ch2, abs(h_ch2), label="Chebyshev-II")
    plt.plot(w_elip, abs(h_elip), label="Elliptic")
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude')

    plt.show()


def main():
    ex_24()


main()
