#! /usr/bin/env python

import matplotlib.pyplot as plt
import control
import numpy as np


def plot_plus(title, xlabel="$\omega/\pi$", ylabel="A($\omega$)"):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.show()


def plot_zpk_from_H(H, title=None, w0=1):
    control.pzmap(H, Plot=True, title=title)
    theta = np.linspace(0, 2*np.pi, 100)
    r = w0
    x1 = r*np.cos(theta)
    x2 = r*np.sin(theta)
    plt.plot(x1, x2, 'r', label=r'$\Omega _0$ = {}'.format(w0))
    plt.legend(fancybox=True, framealpha=1, shadow=True, borderpad=1, fontsize='x-large', bbox_to_anchor=(1, 1))
    plt.grid()
    plt.tight_layout()