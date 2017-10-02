# 1.6.1 単純なグラフの描画
import numpy as np
import matplotlib.pyplot as plt

# create data
x = np.arange(0, 6, 0.1)
y = np.sin(x)

# draw graph
plt.plot(x, y)
plt.show()
