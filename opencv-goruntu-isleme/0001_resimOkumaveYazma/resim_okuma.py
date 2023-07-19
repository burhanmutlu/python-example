import cv2

resim = cv2.imread('cicek.jpg', 0) #gri
#resim = cv2.imread('cicek.jpg', 1) #renkli

cv2.imshow('cicek', resim)
cv2.imwrite('gri.png', resim)

cv2.waitKey(0)
cv2.destroyAllWindows()