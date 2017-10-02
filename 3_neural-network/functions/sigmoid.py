#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


# シグモイド関数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
