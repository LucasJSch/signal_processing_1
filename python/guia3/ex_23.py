#! /usr/bin/env python

# Python native libs
import math
import numpy as np
import control
import matplotlib.pyplot as plt
from scipy.signal import butter, freqs, lp2bp_zpk, zpk2tf


# Project libs
from common.signal_utils import get_N_butterworth, get_w0_range_butterworth
from common.signal_utils import get_parameters_BP_TO_LP, get_transfer_LP_to_BP_butterworth
from common.plot_utils import plot_zpk_from_H

delta_p = 0.1
delta_s1 = 0.05
delta_s2 = 0.07
ws1_bp = 70.0
wp1_bp = 88.0 # This has to be 100, but we adjusted it in order to comply with requirements
wp2_bp = 200.0
ws2_bp = 320.0
w0_bp = 1.0


def ex_23():
    # Transform from BP parameters to LP parameters
    (delta_p_lp, delta_s_lp, wp_lp, ws_lp, w0_lp, B) = get_parameters_BP_TO_LP(delta_p, delta_s1, delta_s2, wp1_bp, wp2_bp, ws1_bp, ws2_bp)
    print (delta_p_lp, delta_s_lp, wp_lp, ws_lp, B)
    # Get LP zeros
    N = get_N_butterworth(delta_p_lp, delta_s_lp, wp_lp, ws_lp)
    w0_lp = min(get_w0_range_butterworth(delta_p_lp, delta_s_lp, wp_lp, ws_lp, N))
    print w0_lp
    (z_lp, p_lp, k_lp) = butter(N, w0_lp, btype='lowpass', analog=True, output='zpk')

    # With LP zeros, get BP transfer function
    # (I.e. make a frequency transformation)
    (z_bp, p_bp, k_bp) = lp2bp_zpk(z_lp, p_lp, k_lp, wo=(wp2_bp + wp1_bp)*0.5, bw=wp2_bp-wp1_bp)
    (num_bp, den_bp) = zpk2tf(z_bp, p_bp, k_bp)
    H = control.tf(num_bp, den_bp)

    # Plot freq. response
    w, h = freqs(num_bp, den_bp)
    plt.plot(w, (abs(h)))
    plt.title('Butterworth filter frequency response')
    plt.xlabel('Frequency [radians / second]')
    plt.ylabel('Amplitude')
    plt.grid(which='both', axis='both')
    # Pass freq. 1
    plt.axvline(wp1_bp, color='red')
    # Pass freq. 2
    plt.axvline(wp2_bp, color='red')
    # Supress freq. 1
    plt.axvline(ws1_bp, color='red')
    # Supress freq. 2
    plt.axvline(ws2_bp, color='red')
    # Pass amp.
    plt.axhline(1 - delta_p_lp, color='green')
    # Supress amp.
    plt.axhline(delta_s_lp, color='green')
    plt.axis([0, 400, 0, 1.1])

    # Plot zeros-poles
    plot_zpk_from_H(H, title='Zeros-poles plot', w0=w0_bp)
    plt.show()


def main():
    ex_23()


main()
