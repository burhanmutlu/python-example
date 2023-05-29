# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:16:57 2023

@author: Burhan Mutlu
"""

import cv2
import numpy as np

class ResimSifreleme:
    
    width=0; height=0; N=13;
    
    def __init__(self, imagePath, renklimi):
        self.imagePath = imagePath
        self.renklimi = renklimi
        self.org = cv2.imread(imagePath,renklimi) 
        self.height= self.org.shape[0];
        self.width= self.org.shape[1];
    
    def getImage(self):
        return self.org
    
    def PrintImage(self, image, title):
        cv2.imshow(title, image)
        self.destroyWindows()
        
    def destroyWindows(self): 
        k=cv2.waitKey(0)
        if k==ord('q'):
            cv2.destroyAllWindows()
            
    def imageEncryption(self):
        encrypted = self.getImage()
        for i in range(self.width):
            for j in range(self.height):
                try:
                    encrypted[j, i ] = self.org[j,i] * self.N     
                except KeyboardInterrupt: 
                    print("You typed CTRL + C, which is the keyboard interrupt exception")
                else:
                    return encrypted
  
    def GetEncrypted(self, j, i):
        val = self.imageEncryption()
        val = val[j,i]
        return int(val)
    
    def imageDecryption(self):
        decrypted = self.getImage()
        for i in range(self.width):
            for j in range(self.height):
                val = self.mod_hesapla( self.GetEncrypted(j,i) )
                decrypted[j, i ] = val
        return decrypted
    
    def mod_hesapla(self, val):
        while 1:
            # if(val<=self.N):
            #     val = val + 256
            if( val%self.N ==0 ):
                return val/(self.N)
            else:
                val = val + 256
                
                
    def test(self):
        print (self.GetEncrypted(10, 10))
                
                
    
          
    