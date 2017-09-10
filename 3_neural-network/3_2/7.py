#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.2.7 ReLU関数
import numpy as np
import matplotlib.pylab as plt
import sys
sys.path.append("../")
from functions import relu


# x軸範囲定義
x = np.arange(-5.0, 5.0, 0.1)


# ReLU関数定義
y = relu.relu(x)


# 画面描画
plt.plot(x, y, label="ReLU")
plt.show()
