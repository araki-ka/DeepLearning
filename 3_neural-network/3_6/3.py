#!/usr/bin/python
# -*- coding: utf-8 -*-


# 3.6.3 バッチ処理


import numpy as np
import common as c


x, _ = c.get_data()
network = c.init_network()
W1, W2, W3 = network["W1"], network["W2"], network["W3"]

print(x.shape)
print(x[0].shape)
print(W1.shape)
print(W2.shape)
print(W3.shape)


x, t = c.get_data()
batch_size = 100
accuracy_cnt = 0

for i in range(0, len(x), batch_size):
    x_batch = x[i:i + batch_size]
    y_batch = c.predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i + batch_size])

print("Accuracy:" + str(float(accuracy_cnt) / len(x)))
