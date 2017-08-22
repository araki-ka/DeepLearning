# 2.5.2 XORゲートの実装
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

# XOR circuit
def _xor(x1, x2):
    s1 = _nand(x1, x2)
    s2 = _or(x1, x2)
    return _and(s1, s2)

# execute
print("----- XOR -----")
print(_xor(0, 0))
print(_xor(1, 0))
print(_xor(0, 1))
print(_xor(1, 1))
