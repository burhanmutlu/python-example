import cv2
import random
import numpy as np

width = 591; height=591

# sifre = cv2.imread("Sifreli1.jpg",1) daha karışık
sifre = cv2.imread("Sifreli.jpg",1)
cozum = np.zeros([width,height,3],dtype=np.uint8)

cv2.imshow("Sifreli",sifre)

def cozme(r, g, b, j, i):
    cozum[j, i, 0] = sifre[j, i, 0] - r
    cozum[j, i, 1] = sifre[j, i, 1] - g 
    cozum[j, i, 2] = sifre[j, i, 2] - b

for i in range(width):
    for j in range(height):
        
        if (j%17==0):
            cozme(60, -60, 60, j, i)
        elif (j%15==0):
            cozme(210, -210, 210, j, i)
        elif (j%13==0):
            cozme(130, -130, 130, j, i)
        elif (j%11==0):
            cozme(240, -240, 240, j, i)
        elif (j%9==0):
            cozme(150, -150, 150, j, i)
        elif (j%7==0):
            cozme(80, -80, 80, j, i)
        elif (j%6==0):
            cozme(45, -45, 45, j, i)
        elif (j%5==0):
            cozme(20, -20, 20, j, i)
        elif (j%4==0):
            cozme(80, -80, 80, j, i)
        elif (j%3==0):
            cozme(200, -200, 200, j, i)
        elif (j%2==0):
            cozme(150, -150, 150, j, i)


cv2.imshow("Cozulmus",cozum)

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("cozulmus.jpg", cozum) 
    cv2.destroyAllWindows()