import string
import cv2
import numpy as np
from matplotlib import pyplot as plt

vid = cv2.VideoCapture(0)
i=0
while(True):
	i = i+1
	ret, frame = vid.read()
	cv2.imshow('frame', frame)
	cv2.imwrite('resim/frame' + str(i)  + '.jpg', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imwrite('frame.jpg', frame)
		break
	int(i)
vid.release()
cv2.destroyAllWindows()

img0 = cv2.imread('frame.jpg',)
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(gray,(3,3),0)

laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  

plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.show()