#! /usr/bin/env python

import numpy as np
import math


def normalized_sinc(w_c, M, t):
    return (w_c / math.pi) * np.sinc((w_c / math.pi) * (t - M/2.0))


# Truncated impulse response of ideal lowpass filter with unitary gain.
# w_c: Cutoff frequency
# M: Order of filter (Length of filter - 1)
def ideal_lowpass_truncated(w_c, M):
    t = np.arange(M + 1)
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

