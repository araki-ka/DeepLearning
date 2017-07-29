# 1.6.3 画像の表示
import matplotlib.pyplot as plt
from matplotlib.image import imread

# 画像セット
img1 = imread("lena.png")
img2 = imread("lena.jpg")

# 1行2列の1番目に描画
plt.subplot(121)
plt.imshow(img1)

# 1行2列の2番目に描画
plt.subplot(122)
plt.imshow(img2)

# 画像描画
plt.show()
