#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np


# ステップ関数
def step_function(x):
    return np.array(x > 0, dtype=np.int)
