#! /usr/bin/env python

import numpy as np
from scipy import fft


def fft_and_normalize_and_to_dB(window, nfft):
    window = np.fft.fftshift(fft(window, nfft))
    window /= window.max()
    window = np.absolute(window)
    20 * np.log10(window)
    return window
