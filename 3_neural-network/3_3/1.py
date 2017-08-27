#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.3.1 多次元配列
import numpy as np


# 1次元配列
A = np.array([1, 2, 3, 4])
print("----- 1次元配列 -----")
print(A)
print(np.ndim(A))
print(A.shape)
print(A.shape[0])


# 2次元配列
B = np.array([[1, 2], [3, 4], [5, 6]])
print("----- 2次元配列 -----")
print(B)
print(np.ndim(B))
print(B.shape)
