#!/usr/bin/env python
# -*- coding: utf-8 -*-

import torch

z = torch.zeros(5, 3)
print(z)
print(z.dtype)


i = torch.ones(5, 3, dtype=torch.int16)
print(i)
print(i.dtype)


torch.manual_seed(1729)
r1 = torch.rand(2, 2)
print("A random tensor: ")
print(r1)
print(r1.dtype)

r2 = torch.rand(2, 2)
print('\nA different random tensor:')
print(r2)
print(r2.dtype)

torch.manual_seed(1729)
r3 = torch.rand(2, 2)
print('\nShould match r1:')
print(r3)
print(r3.dtype)



ones = torch.ones(2, 3)
print("\n ones is")
print(ones)

twos = torch.ones(2, 3) * 2
print("\n twos is")
print(twos)

threes = ones + twos
print("\n threes is")
print(threes)



r = (torch.rand(2, 2) - 0.5) * 2 # values between -1 and 1
print('A random matrix, r:')
print(r)

# Common mathematical operations are supported:
print('\nAbsolute value of r:')
print(torch.abs(r))

# ...as are trigonometric functions:
print('\nInverse sine of r:')
print(torch.asin(r))

# ...and linear algebra operations like determinant and singular value decomposition
print('\nDeterminant of r:')
print(torch.det(r))
print('\nSingular value decomposition of r:')
print(torch.svd(r))

# ...and statistical and aggregate operations:
print('\nAverage and standard deviation of r:')
print(torch.std_mean(r))
print('\nMaximum value of r:')
print(torch.max(r))