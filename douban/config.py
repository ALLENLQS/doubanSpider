
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author  : ALLEN
# @Time    : 2018/12/16 23:43
# @File    : config.py
# @Software: PyCharm

def from_object(obj):
    d = dict()
    for key in dir(obj):
        if key.isupper():
            d[key.lower()] = getattr(obj,key)

    return d