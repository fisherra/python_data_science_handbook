#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:40:27 2018

@author: fisher
"""
import IPython
import numpy as np

# array concat and split

# concat is done by concatenate, hstack, vstack

ar_1 = np.array([1,1,1])

ar_2 = np.array([2,2,2])

ar_3 = np.array([3,3,3])

ar_12 = np.concatenate([ar_1, ar_2])
ar_12h = np.hstack([ar_1, ar_2])
ar_12v = np.vstack([ar_1, ar_2])

print(ar_12)
print(ar_12h)
print(ar_12v)


# can do more than two 

ar_123 = np.vstack([ar_1, ar_2, ar_3])

print(ar_123)

# the opposite of concat is split

# split is done by split, hsplit, vsplit

ar_1s, ar_2s = np.split(ar_12, [4])

print(ar_1s)
print(ar_2s)

# split arrays

ar_4 = np.array.

np.hstack(ar_123)