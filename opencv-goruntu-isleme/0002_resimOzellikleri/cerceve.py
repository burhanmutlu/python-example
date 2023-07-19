import cv2
import numpy as np
from matplotlib import pyplot as plt

mavi = [255,0,0]

img=cv2.imread("cicek.jpg")

replicate=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE,value=mavi)
reflect=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT,value=mavi)
reflect101=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT101,value=mavi)
wrap=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP,value=mavi)
constant=cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=mavi)

plt.subplot(231),plt.imshow(img,"gray"),plt.title("orjinal") #2satır3sutundan1.resim
plt.subplot(232),plt.imshow(replicate,"gray"),plt.title("replicate")
plt.subplot(233),plt.imshow(reflect,"gray"),plt.title("reflect")
plt.subplot(234),plt.imshow(reflect101,"gray"),plt.title("reflect101")
plt.subplot(235),plt.imshow(wrap,"gray"),plt.title("wrap")
plt.subplot(236),plt.imshow(constant,"gray"),plt.title("constant") #2satır3sutundan6.resim

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
