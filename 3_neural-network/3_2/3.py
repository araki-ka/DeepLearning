#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.2.3 ステップ関数のグラフ
import numpy as np
import matplotlib.pylab as plt
import sys
sys.path.append("../")
from functions import step_function as stp


x = np.arange(-5.0, 5.0, 0.1)
y = stp.step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
