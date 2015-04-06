#
# DCP product code
#
# (C) Copyright 2015-2016 Dataculture Analytics Company
# All right reserved.
#
# This file is confidential and NOT open source.  Do not distribute.
#

"""
A number of functions to normalize a range of values.
"""

import numpy as np


def inverted_sigmoid(x, rate=1, cutoff=0):
    """
    An inverted sigmoid such which flattens out at +/- `cutoff` units.
    """
    a = 1.0/(1+np.exp(-cutoff))
    f = a - 1.0/(1 + np.exp(- rate * x))
    return f


def ctd_del_sigmoid(x, rate=1, cutoff=0, y_offset=0.5, x_offest=5):
    """
    a custom sigmoid curve for scoring ctd ~ delivery scores
    """
    a = 1.0/(1+np.exp(-cutoff))
    f = a - 1.0/(1 + np.exp(- rate * (x - x_offest)))
    return f + y_offset


def generalized_sigmoid(x, A=0.0, K=1.0, B=3.0, M=0.0, nu=0.5, Q=0.5):
    f = A + (K - A)/(1 + Q * np.exp(-B * (x - M)))**(1/nu)
    return f

def scale(val, src, dst):
    """
    Scale the given value from the scale of src to the scale of dst.
    """
    return ((val - src[0]) / (src[1]-src[0])) * (dst[1]-dst[0]) + dst[0]

