# -*- coding: utf-8 -*-
"""
Created on Mon May 29 18:58:00 2023

@author: Burhan Mutlu
"""

class Maths:
    
    def mod_hesapla(self, val):
        while 1:
            if(val<=self.N):
                 val = val + 256
            if( val%self.N ==0 ):
                return val/(self.N)
            else:
                val = val + 256

