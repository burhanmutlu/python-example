# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:16:57 2023

@author: Burhan Mutlu
"""

import cv2

class ResimSifreleme:
    
    width=0; height=0; N=41;
    
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
                encrypted[j, i ] = self.org[j,i] * self.N        
        return encrypted
    
    def imageDecryption(self):
        decrypted = self.getImage()
        for i in range(self.width):
            for j in range(self.height):
                val = self.mod_hesapla( decrypted[j,i] )
                decrypted[j, i ] = val
        return decrypted
    
    def mod_hesapla(self, val):
        while 1:
            if(val<=self.N):
                 val = val + 256
            if( val%self.N ==0 ):
                return val/(self.N)
            else:
                val = val + 256
                
                
    def test(self):
        print (self.GetEncrypted(10, 10))
             
        
        