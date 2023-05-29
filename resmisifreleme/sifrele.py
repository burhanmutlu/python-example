import cv2
import random
import numpy as np

width = 591; height=591

img = cv2.imread("org.jpg",1)
sifreli = np.zeros([width,height,3],dtype=np.uint8)

org = cv2.resize(img, (width,height))
cv2.imshow("Orjinal",org)

def sifreleme(r, g, b, j, i):
    sifreli[j, i, 0] = org[j, i, 0] + r
    sifreli[j, i, 1] = org[j, i, 1] + g 
    sifreli[j, i, 2] = org[j, i, 2] + b

for i in range(width):
    for j in range(height):
        
        if (j%17==0):
            sifreleme(60, -60, 60, j, i)
        elif (j%15==0):
            sifreleme(210, -210, 210, j, i)
        elif (j%13==0):
            sifreleme(130, -130, 130, j, i)
        elif (j%11==0):
            sifreleme(240, -240, 240, j, i)
        elif (j%9==0):
            sifreleme(150, -150, 150, j, i)
        elif (j%7==0):
            sifreleme(80, -80, 80, j, i)
        elif (j%6==0):
            sifreleme(45, -45, 45, j, i)
        elif (j%5==0):
            sifreleme(20, -20, 20, j, i)
        elif (j%4==0):
            sifreleme(80, -80, 80, j, i)
        elif (j%3==0):
            sifreleme(200, -200, 200, j, i)
        elif (j%2==0):
            sifreleme(150, -150, 150, j, i)

print(5+-60)
print(5--60)
print(5-+60)

cv2.imshow("Sifreli",sifreli)

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("Sifreli.jpg", sifreli) 
    cv2.destroyAllWindows()