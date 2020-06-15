#! /usr/bin/env python

import math
import numpy as np


def get_beta(A):
    if (A < 0):
        raise Exception("Invalid A: Lower than 0.")
    if (A < 21):
        return 0
    if (A <= 50):
        return 0.5842 * ((A - 21) ** 0.4) + 0.07886 * (A - 21)
    else:
        return 0.1102 * (A - 0.87)


def get_kaiser_window(ripple, delta_w):
    A = -20 * math.log10(ripple)
    beta = get_beta(A)
    M = np.ceil((A - 8) / (2.285 * delta_w))
    return (M, np.kaiser(M + 1, beta))
