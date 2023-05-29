# -*- coding: utf-8 -*-
"""
Created on Mon May 29 19:01:05 2023

@author: Burhan Mutlu
"""

class Window:
    
    def __init__(self):
        pass

    def destroyWindows(self): 
        k=cv2.waitKey(0)
        if k==ord('q'):
            cv2.destroyAllWindows() 