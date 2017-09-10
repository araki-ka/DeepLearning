#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.2.4 シグモイド関数の実装
import numpy as np
import matplotlib.pylab as plt
import sys
sys.path.append("../")
from functions import sigmoid as sig


# データ出力
x = np.array([-1.0, 1.0, 2.0])
print(sig.sigmoid(x))

# シグモイド関数とNumPy配列の具体例
t = np.array([1.0, 2.0, 3.0])
print(1.0 + t)
print(1.0 / t)

# シグモイド関数の描画
x = np.arange(-5.0, 5.0, 0.1)
y = sig.sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
