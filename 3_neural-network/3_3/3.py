#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.3.3 ニューラルネットワークの内積
import numpy as np


X = np.array([1, 2])
W = np.array([[1, 3, 5], [2, 4, 6]])
Y = np.dot(X, W)
print(Y)
