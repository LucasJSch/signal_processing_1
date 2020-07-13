#! /usr/bin/env python

# Python native libs
import math
import numpy as np
import control
import matplotlib.pyplot as plt
from scipy.signal import butter, freqs


# Project libs
from common.signal_utils import get_N_butterworth, get_w0_range_butterworth
from common.signal_utils import get_parameters_HP_TO_LP, get_transfer_LP_to_HP_butterworth
from common.plot_utils import plot_zpk_from_H

delta_p = 0.05
delta_s = 0.2
wp_hp = 200.0
ws_hp = 80.0
w0_hp = 1.0


def ex_22():
    # Transform from HP parameters to LP parameters
    (wp_lp, ws_lp) = get_parameters_HP_TO_LP(wp_hp, ws_hp, w0_hp)
    # Get LP zeros
    N = get_N_butterworth(delta_p, delta_s, wp_lp, ws_lp)
    w0_lp = max(get_w0_range_butterworth(delta_p, delta_s, wp_lp, ws_lp, N))
    (z_lp, p_lp, k_lp) = butter(N, w0_lp, btype='lowpass', analog=True, output='zpk')
    (num_lp, den_lp) = butter(N, w0_lp, btype='lowpass', analog=True, output='ba')
    H_lp = control.tf(num_lp, den_lp)

    # Plot zero-poles for LP
    plot_zpk_from_H(H_lp, title='Zeros-poles plot for LP', w0=w0_lp)

    # Plot freq. response for LP
    w, h = freqs(num_lp, den_lp)
    plt.figure()
    plt.plot(w, (abs(h)))
    plt.title('Butterworth LP filter frequency response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude')
    plt.grid(which='both', axis='both')

    # With LP zeros, get HP transfer function
    # (I.e. make a frequency transformation)
    (num_hp, den_hp) = get_transfer_LP_to_HP_butterworth(p_lp, w0_hp, N)
    H_hp = control.tf(num_hp, den_hp)

    # Plot freq. response for HP
    w, h = freqs(num_hp, den_hp)
    plt.figure()
    plt.plot(w, (abs(h)))
    plt.title('Butterworth HP filter frequency response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude')
    plt.grid(which='both', axis='both')
    # Pass freq.
    plt.axvline(wp_hp, color='red')
    # Supress freq.
    plt.axvline(ws_hp, color='red')
    # Pass amp.
    plt.axhline(1 - delta_p, color='green')
    # Supress amp.
    plt.axhline(delta_s, color='green')
    plt.axis([0, 210, 0, 1.1])

    # Plot zeros-poles for HP
    plot_zpk_from_H(H_hp, title='Zeros-poles plot for HP', w0=w0_hp)
    plt.show()


def main():
    ex_22()


main()
