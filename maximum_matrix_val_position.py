#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 19:15:00 2019

@author: kostya
"""

import numpy as np


A = np.ones((4, 4), int)
A[0, 0] = 5
A[2, 0] = 20
print(A)
print(np.argmax(A))

def max_val_position(A):
    a = np.argmax(A)
    rows, columns = A.shape
    r = int(a/columns)
    c = a%columns
    if a%columns != 0:
        print('A[{}, {}]'.format(r, c), ' = ', A[r, c])
    else:
        print('A[{}, 0]'.format(r), ' = ', A[r, 0])

max_val_position(A)