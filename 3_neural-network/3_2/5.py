#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.2.5 シグモイド関数とステップ関数の比較
import numpy as np
import matplotlib.pylab as plt
from functions import sigmoid as sig
from functions import step_function as stp


# x軸範囲定義
x = np.arange(-5.0, 5.0, 0.1)


# シグモイド関数定義
sigmoid = sig.sigmoid(x)


# ステップ関数定義
step = stp.step_function(x)


# 画面描画
plt.plot(x, sigmoid, label="sigmoid")
plt.plot(x, step, linestyle="--", label="step_function")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
