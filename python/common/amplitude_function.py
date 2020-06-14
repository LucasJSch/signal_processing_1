#! /usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import math

def get_amplitude_func(h, filter_type, M):
  if (filter_type is 1):
    return amplitude_type_1(h, M)
  if (filter_type is 2):
    return amplitude_type_2(h, M)
  if (filter_type is 3):
    return amplitude_type_3(h, M)
  if (filter_type is 4):
    return amplitude_type_4(h, M)


def amplitude_type_1(h, M):
  a = [None] * (M/2 + 1)
  a[0] = h[M/2]
  for i in xrange(1, (M/2) + 1):
    a[i] = 2 * h[(M/2) - i]
  
  def sum(w):
    retval = 0
    for i in xrange(0, (M/2) + 1):
      retval += a[i] * math.cos(w * i)
    return retval

  A_w = lambda w: sum(w)
  return A_w


def amplitude_type_2(h, M):
  b = [None] * (((M+1)/2) + 1)
  b[0] = 0
  for i in xrange(1, ((M+1)/2) + 1):
    b[i] = 2 * h[((M+1)/2) - i]
  
  def sum(w):
    retval = 0
    for i in xrange(1, ((M+1)/2) + 1):
      retval += b[i] * math.cos(w * (i - 0.5))
    return retval

  A_w = lambda w: sum(w)
  return A_w


def amplitude_type_3(h, M):
  c = [None] * ((M/2) + 1)
  c[0] = 0
  for i in xrange(1, (M/2) + 1):
    c[i] = 2 * h[(M/2) - i]
  
  def sum(w):
    retval = 0
    for i in xrange(1, (M/2) + 1):
      retval += c[i] * math.sin(w * i)
    return retval

  A_w = lambda w: sum(w)
  return A_w


def amplitude_type_4(h, M):
  d = [None] * (((M+1)/2) + 1)
  d[0] = 0
  for i in xrange(1, ((M+1)/2) + 1):
    d[i] = 2 * h[((M+1)/2) - i]
  
  def sum(w):
    retval = 0
    for i in xrange(1, ((M+1)/2) + 1):
      retval += d[i] * math.sin(w * (i - 0.5))
    return retval

  A_w = lambda w: sum(w)
  return A_w