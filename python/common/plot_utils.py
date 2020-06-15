#! /usr/bin/env python

import matplotlib.pyplot as plt


def plot_plus(title, xlabel="$\omega/\pi$", ylabel="A($\omega$)"):
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.show()
