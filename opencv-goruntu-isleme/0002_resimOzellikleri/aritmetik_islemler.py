import cv2

img=cv2.imread("saat.jpg")

cv2.imshow("saat", img)

img[80,80] = [255, 255, 255]
print(img[80,80])

bolge=img[30:120, 100:200]
img[30:120, 100:200]=[0,255,255]
img[0:90, 0:100]=bolge
cv2.rectangle(img,(100,30),(200,120),(0,255,255),2)
cv2.imshow("saat2",img)

cv2.waitKey(0)
cv2.destroyAllWindows()