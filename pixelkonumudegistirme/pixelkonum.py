import cv2 
import numpy as np
import random 

width = 400; height=500

imgYeni = np.zeros([500,400,3],dtype=np.uint8)
imgYeni.fill(255)

imgOrg=cv2.imread("barbara.jpg",1)
img = cv2.resize(imgOrg, (width,height))

for i in range(width):
    for j in range(height):
        randX = random.randint(0, width-1) 
        randY = random.randint(0, height-1)
        imgYeni[j][i] = img[randY][randX]


cv2.imshow("eski",img) 
cv2.imshow("yeni", imgYeni)
 
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("yeni.jpg", imgYeni) 
    cv2.destroyAllWindows()