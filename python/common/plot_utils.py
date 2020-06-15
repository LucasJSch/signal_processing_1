#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import math

pi_ticks = ['-$\pi$', '-9$\pi/10$', '-4$\pi/5$', '-7$\pi/10$', '-3$\pi/5$', '-1$\pi/2$', '-2$\pi/5$', '-3$\pi/10$', '-1$\pi/5$', '-1$\pi/10$', '0', '1$\pi/10$',  '1$\pi/5$',  '3$\pi/10$',  '2$\pi/5$',  '1$\pi/2$',  '3$\pi/5$',  '7$\pi/10$',  '4$\pi/5$',  '9$\pi/10$', '$\pi$']


# Plots the current plotted canvas + assigns xtics according to a freq.
# response + grid + legend.
def plot_freq_response():
    plt.legend()
    plt.grid()
    plt.xticks(np.linspace(-np.pi, np.pi, 9), ['-$\pi$', '-$3\pi/4$', '-$\pi/2$', '-$\pi/4$', '0', '$\pi/4$', '$\pi/2$', '$3\pi/4$', '$\pi$'], fontsize=17)
    plt.show()


# The same as above but with dense xticks
def plot_dense_freq_response():
    plt.legend()
    plt.grid()
    plt.xticks(np.linspace(-np.pi, np.pi, len(pi_ticks)), pi_ticks, fontsize=17)
    plt.show()


def plot_plus():
    plt.legend()
    plt.grid()
    plt.show()
