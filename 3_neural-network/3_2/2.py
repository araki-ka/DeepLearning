#!/usr/bin/python
# -*- coding: utf-8 -*-

# 3.2.2 ステップ関数の実装
import numpy as np


def step_function_scalar(inp):
    if inp > 0:
        return 1
    else:
        return 0


def step_function(inp):
    out = inp > 0
    return out.astype(np.int)


print("step_function_scalar")
print("inp = 1 -> ")
print(step_function_scalar(1))
print("inp = -1 -> ")
print(step_function_scalar(-1))

print("step_function")
print("inp = np.array[1.0, 2.0] -> ")
print(step_function(np.array([1.0, 2.0])))
print("inp = np.array[-1.0, -2.0] -> ")
print(step_function(np.array([-1.0, -2.0])))

x = np.array([-1.0, 1.0, 2.0])
y = x > 0
z = y.astype(np.int)
print(x)
print(y)
print(z)
