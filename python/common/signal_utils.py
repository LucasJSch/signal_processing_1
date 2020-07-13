#! /usr/bin/env python

import numpy as np
from scipy import fft
import control
from math import log10, sqrt, ceil


def fft_and_normalize_and_to_dB(window, nfft):
    window = np.fft.fftshift(fft(window, nfft))
    window /= window.max()
    window = np.absolute(window)
    20 * np.log10(window)
    return window


# Returns the N parameter of a filter, given the delta values and
# freq. values
def get_N_butterworth(delta_p, delta_s, wp, ws):
    Ap = -20 * log10(1 - delta_p)
    As = -20 * log10(delta_s)

    # Discrimination factor
    d = sqrt((10 ** (0.1 * Ap) - 1) / (10 ** (0.1 * As) - 1))
    # Selectivity factor
    k = wp/ws

    return ceil(log10(1/d) / log10(1/k))


def get_w0_range_butterworth(delta_p, delta_s, wp, ws, N):
    aux = 1/(1 - delta_p)
    lower_bound = wp * ((aux * aux - 1) ** (-1 / (2 * N)))
    aux = 1/delta_s
    upper_bound = ws * ((aux * aux - 1) ** (-1 / (2 * N)))

    return (lower_bound, upper_bound)


# Returns transformed parameters from Highpass to Lowpass
def get_parameters_HP_TO_LP(wp, ws, w0):
    return (w0/wp, w0/ws)


# Returns transformed parameters from Bandpass to Lowpass
# TODO: Add description.
# Priority can be 'Pass'(P) or 'Supress'(S)
def get_parameters_BP_TO_LP(delta_p, delta_s1, delta_s2, wp1, wp2, ws1, ws2, priority='Pass'):
    delta_s = min(delta_s1, delta_s2)
    if (priority == 'Pass' or priority == 'P'):
        wl = wp1
        wh = wp2
        w0_squared = wl * wh
        B = wh - wl
        wp = 1.0
        aux1 = abs(((ws1*ws1) - w0_squared) / (B * ws1))
        aux2 = abs(((ws2*ws2) - w0_squared) / (B * ws2))
        ws = min(aux1, aux2)
    elif (priority == 'Supress' or priority == 'S'):
        wl = ws1
        wh = ws2
        w0_squared = wl * wh
        B = wh - wl
        ws = 1.0
        aux1 = abs(((wp1*wp1) - w0_squared) / (B * wp1))
        aux2 = abs(((wp2*wp2) - w0_squared) / (B * wp2))
        wp = max(aux1, aux2)
    else:
        raise Exception("Incorrect priority parameter.")
    return (delta_p, delta_s, wp, ws, sqrt(w0_squared), B)


# Returns numerator and denominator coefficientes for the
# equivalent HP filter, given the poles of the LP filter.
def get_transfer_LP_to_HP_butterworth(p_lp, w0_hp, N):
    den_hp = [1.0]
    for pk in p_lp:
        den_hp = np.convolve(den_hp, [1.0, -(w0_hp/pk)])
    num_hp = np.zeros(N+1)
    num_hp[0] = 1.0
    return (num_hp, den_hp)


# Returns numerator and denominator coefficientes for the
# equivalent BP filter, given the poles of the LP filter.
# TODO: Add description
# TODO: Fix. Not working correctly for some reason.
def get_transfer_LP_to_BP_butterworth(p_lp, w0_lp, B, N):
    den_bp = [1.0]
    num_bp = np.zeros(N+1, dtype="complex_")
    num_bp[0] = 1.0
    for pk in p_lp:
        den_bp = np.convolve(den_bp, [1, -B*pk, w0_lp*w0_lp])
        num_bp[0] *= -B*pk
    return (num_bp, den_bp)
