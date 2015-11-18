#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2015 jaidev <jaidev@newton>
#
# Distributed under terms of the MIT license.

"""

"""


def wnv_snowfall_converter(x):
    if x == "T":
        return 0.001
    return x


def wnv_precip_converter(x):
    if x == "T":
        return 0.0001
    return x

mix_grind_col_translate = lambda x: x.replace("row_productfeatures_", "")


def shoes_weight_convert(weight):
    weight = weight.apply(lambda x: x.split()[0])
    return weight.astype(int)
