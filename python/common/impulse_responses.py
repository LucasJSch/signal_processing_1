#! /usr/bin/env python

import numpy as np
import math


# Truncated impulse response of ideal lowpass filter.
# w_c: Cutoff frequency
# M: Order of filter (Length of filter - 1)
def ideal_lowpass_truncated(w_c, M):
    t = np.linspace(0, M, endpoint=True, num=M+1)
    return (w_c / math.pi) * np.sinc((w_c / math.pi) * (t - M/2))
