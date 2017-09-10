#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


# ReLU(Rectified Linear Unit)関数
def relu(x):
    return np.maximum(0, x)
