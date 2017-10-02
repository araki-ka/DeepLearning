# 2.3.3 重みとバイアスによる実装
import numpy as np

# AND circuit
def _and(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# NAND circuit
def _nand(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# OR circuit
def _or(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w * x) + b
    if tmp <= 0:
        return 0
    else:
        return 1

# execute
# AND
print("----- AND -----")
print(_and(0, 0))
print(_and(1, 0))
print(_and(0, 1))
print(_and(1, 1))

# NAND
print("----- NAND -----")
print(_nand(0, 0))
print(_nand(1, 0))
print(_nand(0, 1))
print(_nand(1, 1))

# OR
print("----- OR -----")
print(_or(0, 0))
print(_or(1, 0))
print(_or(0, 1))
print(_or(1, 1))
