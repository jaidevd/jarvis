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
    return [0.001 if _x == 'T' else _x for _x in x]
