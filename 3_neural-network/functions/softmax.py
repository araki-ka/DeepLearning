#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


# ソフトマックス関数
def softmax(a):
    # オーバーフロー対策
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
