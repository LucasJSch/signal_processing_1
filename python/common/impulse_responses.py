#! /usr/bin/env python

import numpy as np
import math
from math import pi


def normalized_sinc(w_c, M, t):
    return (w_c / math.pi) * np.sinc((w_c / math.pi) * (t - M/2.0))


# Truncated impulse response of ideal lowpass filter with unitary gain.
# w_c: Cutoff frequency
# M: Order of filter (Length of filter - 1)
def ideal_lowpass_truncated(w_c, M):
    t = np.arange(0, M + 1)
    return normalized_sinc(w_c, M, t)


# Truncated impulse response of ideal highpass filter with unitary gain.
# w_c: Cutoff frequency
# M: Order of filter (Length of filter - 1)
def ideal_highpass_truncated(w_c, M):
    t = np.arange(0, M + 1)
    return np.sinc(t - M/2.0) - normalized_sinc(w_c, M, t)


# Truncated impulse response of ideal bandpass filter with unitary gain.
# w_c_l: Low cutoff frequency
# w_c_h: High cutoff frequency
# M: Order of filter (Length of filter - 1)
def ideal_bandpass_truncated(w_c_l, w_c_h, M):
    if ((w_c_l > w_c_h) or (w_c_h < 0) or (w_c_l < 0)):
        raise Exception("Invalid frequencies. Check that both are greater than 0 and that w_c_l < w_c_h.")
    t = np.arange(0, M + 1)
    return normalized_sinc(w_c_h, M, t) - normalized_sinc(w_c_l, M, t)


# Truncated impulse response of ideal notch filter with unitary gain.
# w_c_l: Low cutoff frequency
# w_c_h: High cutoff frequency
# M: Order of filter (Length of filter - 1)
def ideal_notch_truncated(w_c_l, w_c_h, M):
    if ((w_c_l > w_c_h) or (w_c_h < 0) or (w_c_l < 0)):
        raise Exception("Invalid frequencies. Check that both are greater than 0 and that w_c_l < w_c_h.")
    return ideal_lowpass_truncated(w_c_l, M) + ideal_highpass_truncated(w_c_h, M)


# Truncated impulse response of ideal multiband filter with indepent gain on each frequency band.
# gains: Vector of gains for each band
# frequencies: Vector of separating frequencies between each band.
# M: Order of filter (Length of filter - 1)
def ideal_multiband_truncated(gains, freqs, M):
    if (len(gains) != (len(freqs)+1)):
        raise Exception("Invalid vectors. Gain vector must have one more element than frequencies vector.")
    N = len(gains)

    h = gains[0] * ideal_lowpass_truncated(freqs[0], M)

    # Sum until one before the end. The final function has a slight difference.
    for i in xrange(1, N-1):
        if (freqs[i] > math.pi):
            raise Exception("Invalid frequency: " + str(freqs[i]))
        h += gains[i] * ideal_bandpass_truncated(freqs[i-1], freqs[i], M)

    h += gains[N-1] * ideal_highpass_truncated(freqs[N-2], M)

    return h


def ideal_hilbert_transformer_truncated(M):
    h = np.zeros(M+1)
    for n in xrange(M + 1):
        if (n == M/2.0):
            h[n] = 0
        else:
            h[n] = (1 - math.cos((n - M/2.0) * math.pi)) / (math.pi * (n - M/2.0))
    return h


def diferentiator(M):
    r = lambda x: x - M/2.0
    n = np.arange(0, M+1)
    h = np.zeros(M+1)
    for i in n:
        if (i == M/2.0):
            h[i] = 0
        else:
            h[i] = (np.cos(pi * r(i)) / r(i)) + ((np.sin(pi * r(i))) / (pi * r(i) * r(i)))
    return h
