#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 19:49:12 2018

@author: fisher
"""

# numpy arrays

import numpy as np 

# numpy array attributes

np.random.seed(0)

# array with random integer between 0 and 10
# array is 6 elements, 2 rows, 3 columns

x1 = np.random.randint(10, size = 6) # One-dimensional array

print(x1)

print(x1[0])

x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array

print(x2)

print(x2[0,0])

x2[0,0] = 3.1415 # will be truncated

print(x2[0,0])

x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array

print(x3)

x3[0,0,0] = 100

print("\n")

print(x3)

# accessing elements through slices

print(x1)

# reverse elements in array

print(x1[::-1])

# first column

print("\n")

print(x2[:,1])

# arrays change their master...

print("\n\n\n")

x4 = np.random.randint(10, size = (2,2))

x5 = x4

print(x4)

print("\n", x5)

x5[0,0] = 1

print(x4)

# thats absurd

# avoid this by using copy method

x6 = x4.copy()


print("\n", x6)

x6 = np.zeros(shape = (2,2))

print("\n", x6)

# don't forget the copy method 

x6.copy()

# reshape method

x6 = x6.reshape((4,1))

print(x6)

x6 = x6.reshape((1,4))

print(x6)
