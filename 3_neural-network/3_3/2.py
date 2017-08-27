#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.3.2 行列の内積
import numpy as np


# [2 x 2] * [2 x 2]
print("----- [2 x 2] * [2 x 2] -----")
A = np.array([[1, 2], [3, 4]])
print(A.shape)
B = np.array([[5, 6], [7, 8]])
print(B.shape)
print(np.dot(A, B))


# [2 x 3] * [3 x 2]
print("----- [2 x 3] * [3 x 2] -----")
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.shape)
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B.shape)
print(np.dot(A, B))


# # (error)[2 x 3] * [2 x 2]
# print("----- [2 x 3] * [2 x 2] -----")
# C = np.array([[1, 2], [3, 4]])
# print(C.shape)
# print(np.dot(A, C))


# [2 x 3] * [1 x 2]
print("----- [2 x 3] * [1 x 2] -----")
A = np.array([[1, 2], [3, 4], [5, 6]])
print(A.shape)
B = np.array([7, 8])
print(B.shape)
print(np.dot(A, B))
