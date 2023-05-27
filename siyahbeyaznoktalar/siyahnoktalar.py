import cv2 
import numpy as np
import random 

width = 400; height=500

img2=cv2.imread("barbara.jpg",1)
img = cv2.resize(img2, (width,height))
for i in range(200):
    for j in range(200):
        randX = random.randint(0, width -1)
        randY = random.randint(0, height -1)
        if(j%2 == 0):
            img[randY][randX] = 0
        else:
            img[randY][randX] = 255


cv2.imshow("Siyah Noktalar Olusturma",img) 

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("yeni.jpg", img) 
    cv2.destroyAllWindows()