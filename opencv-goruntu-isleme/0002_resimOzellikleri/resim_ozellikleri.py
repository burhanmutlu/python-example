import cv2
import numpy as np

img = cv2.imread('cicek.jpg',1)
print(str(img.item(100,100,2))) #bu noktadaki kırmızı değer
# bgr 0 1 2 2=kırmızı 1=yeşil 0=mavi
img.itemset((100,100,2),255) # belli noktanın rengini değiştirme

print("resim boyutları" + str(img.shape))
if len(img.shape)==3:
    print("renkli")
elif len(img.shape)==2:
    print("gri")
    
print("resmin pixel boyutu: " + str(img.size))

print("veri tipi"+str(img.dtype))

ROI=img[200:400,200:350] #y,x
cv2.imshow("roi", ROI)

img[200:400,100:250]=ROI #resmin belli noktalarına roiyi kopyala

""" b,g,r=cv2.split(img) bu sistemi yoruyor
img=cv2.merge((b,g,r)) """

img[:,:,2]=0 #0 1 2 kırmızı değerleri sildi 0 yaptı

cv2.imshow('resim',img)
cv2.waitKey()
cv2.destroyAllWindows()