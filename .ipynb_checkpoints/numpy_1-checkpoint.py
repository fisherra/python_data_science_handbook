#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 15:03:49 2018

@author: fisher
"""

# Loading, storing, manipulating data

import numpy as np

li = list(range(10))

print(li)

print(type(li[0]))

# turn li into a list of strings

li_2 = [str(c) for c in li] 

print(li_2)

print(type(li[0]))

# can create hetrogeneous lists

li_3 = [True, "yes", 1, 1.512]

print(li_3)

for item in li_3:
    print(type(item))

# array in python
    
import array 

li_4 = list(range(10))

ar_1 = array.array("i", li_4)

print(ar_1)

# numpy array

ar_2 = np.array([1,2,3,4,5])

print(ar_2)

# must be same type of element

# some array examples

print(np.zeros(10))

print(np.ones((3,5)))

print(np.arange(2,20,1))

print(np.random.random((3,3)))






