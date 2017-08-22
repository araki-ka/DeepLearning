# 2.3.2 重みとバイアスの導入
import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

# [x1, x2] * [w1, w2] -> [x1 * w1, x2 * w2]
print(w * x)

# x1 * w1 + x2 * w2
print(np.sum(w * x))

# x1 * w1 + x2 * w2 + b
print(np.sum(w * x) + b)
