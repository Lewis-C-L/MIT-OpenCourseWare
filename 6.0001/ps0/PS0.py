#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:19:50 2020

@author: lewisling
"""
import numpy as np

print("Enter number x:")
x = int(input())            # takes integer input for x


print("Enter number y:")
y = int(input())            # takes integer input for y

z0  = x**y
z1 = np.log2(x)

print("X**y =" ,z0)
print("log(x) =" ,z1)
