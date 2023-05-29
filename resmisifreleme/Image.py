# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:54:22 2023

@author: Burhan Mutlu
"""

class Image:
    
    width=0
    height=0
    imagePath=""
    isColorful=0
    
    def __init__(self, imagePath, renklimi):
        self.imagePath = imagePath
        self.renklimi = renklimi
        self.org = cv2.imread(imagePath,renklimi) 
        self.height= self.org.shape[0];
        self.width= self.org.shape[1];
        
    def getImage(self):
        return self.org

    def setImage(self):
        
    