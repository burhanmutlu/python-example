# -*- coding: utf-8 -*-
"""
Created on Mon May 29 12:04:22 2023

@author: Burhan Mutlu
"""

from turtle import width
import cv2
import random
import numpy as np

def mod_hesapla(val):
    while 1:
        if(val<=N):
            val = val + 256
        if( val%N ==0 ):
            return val/N
        else:
            val = val + 256

img = cv2.imread("org.jpg",0)
sifreli = img
height= img.shape[0];
width= img.shape[1];

cv2.imshow("orginal:", img)


N = 13
for i in range(width):
    for j in range(height):
        sifreli[j, i ] = img[j,i] * N 
        
cv2.imshow("Sifreli",sifreli)


for i in range(width):
    for j in range(height):
        val = mod_hesapla( sifreli[j, i ] )
        img[j, i ] = val
        

cv2.imshow("cozulmus",img)


k=cv2.waitKey(0)
if k==ord('q'):
    cv2.imwrite("Sifreli.png", sifreli) 
    cv2.destroyAllWindows()
     