from turtle import width
import cv2
import random
import numpy as np


img = cv2.imread("org.png",1)
height= img.shape[0];
width= img.shape[1];

sifreli = np.zeros([height,width,3],dtype=np.uint8)
cozulmus = np.zeros([height,width,3],dtype=np.uint8)
cv2.imshow("orginal:", img)

for i in range(width):
    for j in range(height):
            sifreli[(7*j+5) % height,(90*i+2) % width ] = img[j,i]

""" for i in range(width):
    for j in range(height):
            cozulmus[(j/7-5) % height,(i/90-2) % width ] = sifreli[j,i]
 """

        



cv2.imshow("Sifreli",sifreli)
cv2.imshow("Cozulmus",cozulmus)

k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("Sifreli.png", sifreli) 
    cv2.destroyAllWindows()