# -*- coding: utf-8 -*-
"""005.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1XFPo0ZFkAoco4iMAUwdU9TE7kJj8_rve
"""

import cv2
from skimage.filters import sobel

img = cv2.imread("",0)
img2=sobel(img)

cv2.imshow("pic",img)
cv2.imshow("edge",img2)

print(img.shape)

cv2.waitkey(0)
cv2.destroyAllWindows()