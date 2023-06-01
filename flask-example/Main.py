# -*- coding: utf-8 -*-
"""
Created on Mon May 29 14:28:47 2023

@author: Burhan Mutlu
"""

from moduleFile import ResimSifreleme

p = ResimSifreleme("org.jpg", 0)

sifreli = p.imageEncryption()
p.PrintImage(sifreli, "sifreli")


cozulmus = p.imageDecryption()
p.PrintImage(cozulmus, "cozulmus")
